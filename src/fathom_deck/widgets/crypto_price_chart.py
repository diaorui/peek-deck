"""Crypto price chart widget using Binance US candles API."""

from datetime import datetime, timezone
from typing import Any, Dict, List

from ..core.base_widget import BaseWidget
from ..core.http_cache import get_http_client


class CryptoPriceChartWidget(BaseWidget):
    """Displays cryptocurrency price history chart using candlestick data.

    Required params:
        - symbol: Trading pair symbol (e.g., "BTCUSD", "ETHUSD")
        - tabs: List of tab configurations with interval, limit, and label
          Supported intervals: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
    """

    def get_required_params(self) -> list[str]:
        return ["symbol", "tabs"]

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch candlestick data for all configured tabs."""
        self.validate_params()

        symbol = self.merged_params["symbol"].upper()
        tabs_config = self.merged_params["tabs"]
        client = get_http_client()

        # Fetch data for all tabs
        all_tabs_data = []
        for tab_config in tabs_config:
            interval = tab_config.get("interval", "1d")
            limit = tab_config.get("limit", 30)
            label = tab_config.get("label", interval)

            tab_data = self._fetch_single_chart(symbol, interval, limit)
            tab_data["label"] = label
            all_tabs_data.append(tab_data)

        data = {
            "symbol": symbol,
            "tabs": all_tabs_data,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
        print(f"✅ Fetched {len(all_tabs_data)} tabs for {symbol}")
        return data

    def _fetch_single_chart(self, symbol: str, interval: str, limit: int) -> Dict[str, Any]:
        """Fetch data for a single chart from Binance US."""
        client = get_http_client()
        try:
            # Fetch candlestick data from Binance US API
            url = "https://api.binance.us/api/v3/klines"
            params = {
                "symbol": symbol,
                "interval": interval,
                "limit": limit
            }
            candles = client.get(url, params=params, response_type="json")

            # Binance returns candles in chronological order (oldest first)
            # Parse candles into structured format
            # Binance format: [OpenTime, Open, High, Low, Close, Volume, CloseTime, QuoteVolume, NumTrades, TakerBuyBase, TakerBuyQuote, Ignore]
            parsed_candles = []
            for candle in candles:
                parsed_candles.append({
                    "timestamp": candle[0],  # Open time in milliseconds
                    "open": float(candle[1]),
                    "high": float(candle[2]),
                    "low": float(candle[3]),
                    "close": float(candle[4]),
                    "volume": float(candle[5])
                })

            return {
                "interval": interval,
                "candles": parsed_candles,
            }

        except Exception as e:
            print(f"❌ Failed to fetch or parse candles for {symbol}: {e}")
            raise

    def render(self, processed_data: Dict[str, Any]) -> str:
        """Render tabbed price chart widget HTML with Chart.js."""
        symbol = processed_data["symbol"]
        tabs_data = processed_data["tabs"]
        fetched_at = processed_data["fetched_at"]

        # Format the symbol for better readability
        base_currency = symbol[:3]
        if base_currency == "BTC":
            display_name = "Bitcoin"
        elif base_currency == "ETH":
            display_name = "Ethereum"
        elif base_currency == "SOL":
            display_name = "Solana"
        else:
            display_name = base_currency

        # Generate tab buttons
        tab_buttons = []
        for i, tab_data in enumerate(tabs_data):
            active_class = "active" if i == 0 else ""
            label = tab_data["label"]
            tab_buttons.append(
                f'<button class="chart-tab-btn {active_class}" data-tab="tab-{i}">{label}</button>'
            )

        # Generate tab contents with charts
        tab_contents = []
        chart_scripts = []

        for i, tab_data in enumerate(tabs_data):
            interval = tab_data["interval"]
            candles = tab_data["candles"]

            # Prepare data for Chart.js
            # Pass timestamps to JavaScript for client-side timezone conversion
            timestamps = []
            prices = []
            for candle in candles:
                timestamps.append(candle["timestamp"])
                prices.append(candle["close"])

            # Generate unique ID for this chart
            chart_id = f"chart-{symbol.lower()}-tab-{i}"

            # Show first tab, hide others
            display_style = "" if i == 0 else "display: none;"

            # Tab content HTML
            tab_content = f"""
        <div class="chart-tab-content" data-tab-id="tab-{i}" style="{display_style}">
            <div class="widget-body">
                <canvas id="{chart_id}"></canvas>
            </div>
            <div class="widget-footer">
                <small data-timestamp="{fetched_at}">Updated {fetched_at}</small>
            </div>
        </div>"""
            tab_contents.append(tab_content)

            # Chart.js script
            chart_script = f"""
        <script>
        (function() {{
            const ctx = document.getElementById('{chart_id}').getContext('2d');
            const timestamps = {timestamps};
            const interval = '{interval}';

            // Convert timestamps to user's local timezone
            const labels = timestamps.map(ts => {{
                const date = new Date(ts);
                // Daily intervals: show date only
                if (interval === '1d' || interval === '3d' || interval === '1w' || interval === '1M') {{
                    return date.toLocaleDateString('en-US', {{ month: 'short', day: 'numeric' }});
                }}
                // Multi-hour intervals: show date + time
                else if (interval === '2h' || interval === '4h' || interval === '6h' || interval === '8h' || interval === '12h') {{
                    return date.toLocaleDateString('en-US', {{ month: 'short', day: 'numeric' }}) + ' ' +
                           date.toLocaleTimeString('en-US', {{ hour: '2-digit', minute: '2-digit', hour12: false }});
                }}
                // Minute and hourly intervals: show time only
                else {{
                    return date.toLocaleTimeString('en-US', {{ hour: '2-digit', minute: '2-digit', hour12: false }});
                }}
            }});

            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: labels,
                    datasets: [{{
                        label: '{symbol} Price',
                        data: {prices},
                        borderColor: 'rgb(247, 147, 26)',
                        backgroundColor: 'rgba(247, 147, 26, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.1
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            display: false
                        }},
                        tooltip: {{
                            mode: 'index',
                            intersect: false,
                            callbacks: {{
                                label: function(context) {{
                                    return '$' + context.parsed.y.toLocaleString('en-US', {{
                                        minimumFractionDigits: 2,
                                        maximumFractionDigits: 2
                                    }});
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            ticks: {{
                                color: '#9ca3af',
                                callback: function(value) {{
                                    return '$' + value.toLocaleString();
                                }}
                            }},
                            grid: {{
                                color: 'rgba(255, 255, 255, 0.1)'
                            }}
                        }},
                        x: {{
                            ticks: {{
                                color: '#9ca3af',
                                maxRotation: 45,
                                minRotation: 45
                            }},
                            grid: {{
                                color: 'rgba(255, 255, 255, 0.1)'
                            }}
                        }}
                    }}
                }}
            }});
        }})();
        </script>"""
            chart_scripts.append(chart_script)

        # Render using template
        return self.render_template(
            "widgets/crypto_price_chart.html",
            size=self.size,
            display_name=display_name,
            tab_buttons=tab_buttons,
            tab_contents=tab_contents,
            chart_scripts=chart_scripts
        )
