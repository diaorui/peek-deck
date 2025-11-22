"""Stage 3: Render HTML from processed data."""

import json
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from .core.cache import Cache
from .core.loader import (
    discover_all_pages,
    load_page_config,
    create_widget_instance
)


def render_all():
    """Render HTML pages from processed data."""
    project_root = Path.cwd()
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

    # Discover all pages
    page_files = discover_all_pages()
    if not page_files:
        print("❌ No pages found in pages/ directory")
        return

    print(f"📄 Found {len(page_files)} page(s)\n")

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

        print(f"📄 Rendering: {page_config.id} ({page_config.name}) [{page_config.category}]")

        # Render each widget
        widget_htmls = []
        for widget_config in page_config.widgets:
            widget_type = widget_config.type

            # Generate cache key
            cache_key = cache.get_cache_key(
                page_config.category,
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
                widget_htmls.append(widget_html)
            except Exception as e:
                print(f"    ❌ Failed to render {widget_type}: {e}")
                continue

        # Render page
        try:
            template = env.get_template("pages/page.html")
            # Use page's theme if defined, otherwise use default theme
            page_theme = page_config.theme if page_config.theme else {}
            page_html = template.render(
                page=page_config,
                theme=page_theme,
                widgets=widget_htmls,
                generated_at=datetime.now().isoformat()
            )

            # Save page HTML to flat structure: docs/{page_id}.html
            page_output = docs_dir / f"{page_config.id}.html"
            with open(page_output, 'w') as f:
                f.write(page_html)

            print(f"    ✅ Saved to {page_config.id}.html")
            rendered_pages += 1

        except Exception as e:
            print(f"    ❌ Failed to render page: {e}")
            failed_pages += 1

    # Print summary
    print(f"\n{'='*60}")
    print(f"📊 Render Summary:")
    print(f"   ✅ Rendered: {rendered_pages} pages")
    print(f"   ❌ Failed: {failed_pages} pages")
    print(f"   📁 Output: {docs_dir}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    render_all()
