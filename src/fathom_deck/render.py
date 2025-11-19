"""Stage 3: Render HTML from processed data."""

import json
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from .core.cache import Cache
from .core.loader import (
    discover_pages,
    load_page_config,
    load_series_config,
    create_widget_instance
)


def _create_tabbed_chart_widget(tabs, size, display_name):
    """Create a tabbed chart widget wrapper."""
    # Generate tab buttons
    tab_buttons = []
    for i, tab in enumerate(tabs):
        active_class = "active" if i == 0 else ""
        tab_buttons.append(
            f'<button class="chart-tab-btn {active_class}" data-tab="{tab["tab_id"]}">{tab["tab_label"]}</button>'
        )

    tab_buttons_html = "\n                ".join(tab_buttons)

    # Generate tab contents
    tab_contents = [tab["content"] for tab in tabs]
    tab_contents_html = "\n        ".join(tab_contents)

    # Create wrapper
    html = f"""
        <div class="widget widget-crypto-price-chart widget-{size}">
            <div class="widget-header">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3>{display_name} Price Chart</h3>
                    <div class="chart-tabs">
                        {tab_buttons_html}
                    </div>
                </div>
            </div>
            {tab_contents_html}
        </div>
    """
    return html


def render_all():
    """Render HTML pages from processed data."""
    project_root = Path.cwd()
    series_dir = project_root / "series"
    data_processed_dir = project_root / "data" / "processed"
    docs_dir = project_root / "docs"
    cache_dir = project_root / "data" / "cache"
    templates_dir = project_root / "templates"

    # Create directories
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Initialize cache
    cache = Cache(cache_dir)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(templates_dir))

    print("🎨 Stage 3: Rendering HTML pages\n")

    # Track stats
    rendered_pages = 0
    failed_pages = 0

    # Discover all series
    if not series_dir.exists():
        print(f"❌ Series directory not found: {series_dir}")
        return

    for series_path in series_dir.iterdir():
        if not series_path.is_dir():
            continue

        series_id = series_path.name
        print(f"\n📁 Series: {series_id}")

        # Load series config
        series_config = load_series_config(series_path)

        # Create series output directory
        series_docs_dir = docs_dir / series_id
        series_docs_dir.mkdir(parents=True, exist_ok=True)

        # Discover pages in this series
        page_files = discover_pages(series_path)

        for page_file in page_files:
            # Load page config
            try:
                page_config = load_page_config(page_file)
            except Exception as e:
                print(f"❌ Failed to load {page_file.name}: {e}")
                failed_pages += 1
                continue

            if not page_config.enabled:
                continue

            print(f"  📄 Rendering: {page_config.id} ({page_config.name})")

            # Render each widget
            widget_htmls = []
            chart_tabs = []  # Collect chart widgets with tab_id
            chart_tab_size = None
            chart_display_name = None

            for widget_config in page_config.widgets:
                widget_type = widget_config.type

                # Generate cache key
                cache_key = cache.get_cache_key(
                    series_id,
                    page_config.id,
                    widget_type,
                    widget_config.params
                )

                # Load processed data
                processed_file = data_processed_dir / f"{cache_key}.json"
                if not processed_file.exists():
                    print(f"    ⚠️  No processed data for {widget_type}, skipping")
                    continue

                try:
                    with open(processed_file, 'r') as f:
                        processed_data = json.load(f)
                except Exception as e:
                    print(f"    ❌ Failed to read {processed_file.name}: {e}")
                    continue

                # Create widget instance
                try:
                    widget = create_widget_instance(
                        widget_type=widget_type,
                        size=str(widget_config.size),
                        params=widget_config.params,
                        page_params=page_config.params,
                        update_minutes=widget_config.update_minutes
                    )
                except Exception as e:
                    print(f"    ❌ Failed to create widget {widget_type}: {e}")
                    continue

                # Render widget HTML
                try:
                    widget_html = widget.render(processed_data)

                    # Check if this is a chart widget with tab_id
                    tab_id = widget_config.params.get("tab_id", "")
                    tab_label = widget_config.params.get("tab_label", "")

                    if widget_type == "crypto-price-chart" and tab_id:
                        # Collect tab info
                        if chart_tab_size is None:
                            chart_tab_size = widget_config.size
                            # Extract display name from processed data
                            symbol = processed_data.get("symbol", "")
                            base_currency = symbol[:3] if symbol else ""
                            if base_currency == "BTC":
                                chart_display_name = "Bitcoin"
                            elif base_currency == "ETH":
                                chart_display_name = "Ethereum"
                            elif base_currency == "SOL":
                                chart_display_name = "Solana"
                            else:
                                chart_display_name = base_currency

                        chart_tabs.append({
                            "tab_id": tab_id,
                            "tab_label": tab_label,
                            "content": widget_html
                        })
                    else:
                        # Flush any collected tabs before adding regular widget
                        if chart_tabs:
                            tabbed_widget = _create_tabbed_chart_widget(chart_tabs, chart_tab_size, chart_display_name)
                            widget_htmls.append(tabbed_widget)
                            chart_tabs = []
                            chart_tab_size = None
                            chart_display_name = None

                        widget_htmls.append(widget_html)
                except Exception as e:
                    print(f"    ❌ Failed to render {widget_type}: {e}")
                    continue

            # Flush any remaining tabs
            if chart_tabs:
                tabbed_widget = _create_tabbed_chart_widget(chart_tabs, chart_tab_size, chart_display_name)
                widget_htmls.append(tabbed_widget)

            # Render page
            try:
                template = env.get_template("pages/page.html")
                page_html = template.render(
                    page=page_config,
                    theme=series_config.theme,
                    widgets=widget_htmls,
                    generated_at=datetime.now().isoformat()
                )

                # Save page HTML
                page_output = series_docs_dir / f"{page_config.id}.html"
                with open(page_output, 'w') as f:
                    f.write(page_html)

                print(f"    ✅ Saved to {page_output.relative_to(docs_dir)}")
                rendered_pages += 1

                # Mark all widgets as updated in cache (only after successful render)
                for widget_config in page_config.widgets:
                    cache_key = cache.get_cache_key(
                        series_id,
                        page_config.id,
                        widget_config.type,
                        widget_config.params
                    )
                    cache.mark_updated(cache_key)

            except Exception as e:
                print(f"    ❌ Failed to render page: {e}")
                failed_pages += 1

    # Save cache
    cache.save()

    # Print summary
    print(f"\n{'='*60}")
    print(f"📊 Render Summary:")
    print(f"   ✅ Rendered: {rendered_pages} pages")
    print(f"   ❌ Failed: {failed_pages} pages")
    print(f"   📁 Output: {docs_dir}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    render_all()
