"""Crypto price chart widget using Gemini candles API."""

import requests
from datetime import datetime
from typing import Any, Dict, List
from tenacity import retry, stop_after_attempt, wait_exponential

from ..core.base_widget import BaseWidget
from ..core.http_cache import get_cached, cache_response


class CryptoPriceChartWidget(BaseWidget):
    """Displays cryptocurrency price history chart using candlestick data.

    Required params:
        - symbol: Trading pair symbol (e.g., "btcusd", "ethusd")

    Optional params:
        - timeframe: Chart timeframe - "1h", "6h", "1day" (default: "1day")
        - limit: Number of candles to fetch (default: 30)
    """

    def get_required_params(self) -> list[str]:
        return ["symbol"]

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    def _fetch_candles(self, symbol: str, timeframe: str) -> List[List]:
        """Fetch candlestick data from Gemini API.

        Returns: List of [timestamp_ms, open, high, low, close, volume]
        """
        url = f"https://api.gemini.com/v2/candles/{symbol}/{timeframe}"

        # Check cache first
        cached = get_cached(url)
        if cached:
            print(f"✅ Cache hit: {url}")
            return cached

        print(f"📡 Fetching: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Cache the response
        cache_response(url, data)
        return data

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch candlestick data for price chart."""
        self.validate_params()

        symbol = self.merged_params["symbol"].lower()
        timeframe = self.merged_params.get("timeframe", "1day")
        limit = self.merged_params.get("limit", 30)

        try:
            candles = self._fetch_candles(symbol, timeframe)

            # Gemini returns candles in descending order (newest first)
            # Reverse for chronological order
            candles = list(reversed(candles))

            # Limit to requested number of candles
            if limit:
                candles = candles[-limit:]

            # Parse candles into structured format
            parsed_candles = []
            for candle in candles:
                parsed_candles.append({
                    "timestamp": candle[0],
                    "open": float(candle[1]),
                    "high": float(candle[2]),
                    "low": float(candle[3]),
                    "close": float(candle[4]),
                    "volume": float(candle[5])
                })

            data = {
                "symbol": symbol.upper(),
                "timeframe": timeframe,
                "candles": parsed_candles,
                "fetched_at": datetime.now().isoformat(),
            }

            print(f"✅ Fetched {len(parsed_candles)} candles for {symbol.upper()} ({timeframe})")
            return data

        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch candles for {symbol} from Gemini: {e}")
            raise
        except (KeyError, ValueError, IndexError) as e:
            print(f"❌ Failed to parse Gemini candles response for {symbol}: {e}")
            raise

    def render(self, processed_data: Dict[str, Any]) -> str:
        """Render price chart widget HTML with Chart.js."""
        symbol = processed_data["symbol"]
        timeframe = processed_data["timeframe"]
        candles = processed_data["candles"]

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

        # Format timeframe for display based on candle count
        num_candles = len(candles)
        if timeframe == "1day":
            timeframe_display = f"{num_candles} Days"
        elif timeframe == "6h":
            days = num_candles // 4  # 4 candles per day for 6h timeframe
            timeframe_display = f"{days} Days"
        elif timeframe == "1hr":
            hours = num_candles
            timeframe_display = f"{hours} Hours"
        else:
            timeframe_display = timeframe

        # Prepare data for Chart.js
        labels = []
        prices = []
        for candle in candles:
            # Format timestamp based on timeframe
            timestamp = candle["timestamp"]
            dt = datetime.fromtimestamp(timestamp / 1000)  # Convert from ms

            if timeframe == "1day":
                label = dt.strftime("%b %d")  # "Nov 19"
            elif timeframe == "6h":
                label = dt.strftime("%b %d %H:%M")
            else:  # 1h, etc.
                label = dt.strftime("%H:%M")

            labels.append(label)
            prices.append(candle["close"])

        # Get ISO timestamp for client-side formatting
        timestamp_iso = processed_data['fetched_at']

        # Get tab configuration if provided
        tab_id = self.merged_params.get("tab_id", "")
        tab_label = self.merged_params.get("tab_label", timeframe_display)

        # Generate unique ID for this chart
        chart_id = f"chart-{symbol.lower()}-{timeframe}-{num_candles}"

        # Determine if this is a tab (has tab_id) or standalone
        if tab_id:
            # This is part of a tabbed interface
            # The first tab should be active by default
            is_first_tab = tab_id == "24h"
            display_style = "" if is_first_tab else "display: none;"

            html = f"""
        <div class="chart-tab-content" data-tab-id="{tab_id}" style="{display_style}">
            <div class="widget-body">
                <canvas id="{chart_id}"></canvas>
            </div>
            <div class="widget-footer">
                <small data-timestamp="{timestamp_iso}">Updated {timestamp_iso}</small>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
        <script>
        (function() {{
            const ctx = document.getElementById('{chart_id}').getContext('2d');
            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: {labels},
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
                    maintainAspectRatio: true,
                    aspectRatio: 2,
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
        </script>
        """
        else:
            # Standalone chart widget (backward compatible)
            html = f"""
        <div class="widget widget-crypto-price-chart widget-{self.size}">
            <div class="widget-header">
                <h3>{display_name} Price Chart ({timeframe_display})</h3>
            </div>
            <div class="widget-body">
                <canvas id="{chart_id}"></canvas>
            </div>
            <div class="widget-footer">
                <small data-timestamp="{timestamp_iso}">Updated {timestamp_iso}</small>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
        <script>
        (function() {{
            const ctx = document.getElementById('{chart_id}').getContext('2d');
            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: {labels},
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
                    maintainAspectRatio: true,
                    aspectRatio: 2,
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
        </script>
        """
        return html.strip()
