"""Utility functions for FathomDeck."""

from datetime import datetime


def format_time_ago(timestamp_str: str) -> str:
    """Convert ISO timestamp to relative time string.

    Args:
        timestamp_str: ISO format timestamp (e.g., "2025-01-15T10:30:00")

    Returns:
        Human-readable relative time (e.g., "5m ago", "2h ago", "3d ago")
    """
    try:
        # Parse ISO timestamp (handle both with and without microseconds)
        if '.' in timestamp_str:
            timestamp = datetime.fromisoformat(timestamp_str.split('.')[0])
        else:
            timestamp = datetime.fromisoformat(timestamp_str)

        now = datetime.now()
        delta = now - timestamp

        # Calculate time difference
        seconds = delta.total_seconds()

        if seconds < 0:
            return "just now"

        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24

        if seconds < 60:
            return f"{int(seconds)}s ago"
        elif minutes < 60:
            return f"{int(minutes)}m ago"
        elif hours < 24:
            return f"{int(hours)}h ago"
        elif days < 30:
            return f"{int(days)}d ago"
        else:
            months = days / 30
            return f"{int(months)}mo ago"

    except Exception as e:
        # Fallback to original timestamp if parsing fails
        return timestamp_str[:19]


def format_currency(value: float, decimals: int = 2) -> str:
    """Format a number as currency with commas and decimals.

    Args:
        value: Number to format
        decimals: Number of decimal places (default: 2)

    Returns:
        Formatted string (e.g., "$45,000.00")
    """
    return f"${value:,.{decimals}f}"


def format_large_number(value: float) -> str:
    """Format large numbers with K, M, B suffixes.

    Args:
        value: Number to format

    Returns:
        Formatted string (e.g., "1.5M", "2.3B")
    """
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.2f}K"
    else:
        return f"${value:.2f}"
