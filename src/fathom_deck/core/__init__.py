"""Core framework components."""

from .base_widget import BaseWidget, WidgetData
from .cache import Cache
from .config import PageConfig, SeriesConfig, ThemeConfig, WidgetConfig
from .http_cache import HTTPClient, get_http_client

__all__ = [
    "BaseWidget",
    "WidgetData",
    "Cache",
    "PageConfig",
    "SeriesConfig",
    "ThemeConfig",
    "WidgetConfig",
    "HTTPClient",
    "get_http_client",
]
