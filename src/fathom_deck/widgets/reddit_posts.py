"""Reddit posts widget using Reddit RSS feed."""

import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any, Dict, List

from ..core.base_widget import BaseWidget
from ..core.http_cache import get_http_client


class RedditPostsWidget(BaseWidget):
    """Displays recent posts from a subreddit.

    Required params:
        - subreddit: Subreddit name (e.g., "artificial", "bitcoin")

    Optional params:
        - limit: Number of posts to show (default: 10)
        - timeframe: Time filter for top posts - "day", "week", "month", "year", "all" (default: "day")
    """

    def get_required_params(self) -> list[str]:
        return ["subreddit"]

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch recent posts from subreddit RSS feed."""
        self.validate_params()

        subreddit = self.merged_params["subreddit"]
        limit = self.merged_params.get("limit", 10)
        timeframe = self.merged_params.get("timeframe", "day")
        client = get_http_client()

        try:
            # Fetch RSS feed from Reddit (top posts only)
            url = f"https://www.reddit.com/r/{subreddit}/top.rss"
            params = {"t": timeframe}
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; FeedReader/1.0)"
            }
            xml_data = client.get(url, params=params, headers=headers, response_type="text")

            # Parse XML (Atom format)
            root = ET.fromstring(xml_data)
            ns = {'atom': 'http://www.w3.org/2005/Atom', 'media': 'http://search.yahoo.com/mrss/'}
            entries = root.findall('atom:entry', ns)

            # Extract posts
            posts = []
            for entry in entries[:limit]:
                title_elem = entry.find('atom:title', ns)
                link_elem = entry.find('atom:link', ns)
                author_elem = entry.find('atom:author/atom:name', ns)
                published_elem = entry.find('atom:published', ns)
                thumbnail_elem = entry.find('media:thumbnail', ns)

                if title_elem is None or link_elem is None:
                    continue

                # Parse timestamp
                published_timestamp = None
                if published_elem is not None and published_elem.text:
                    try:
                        dt = datetime.fromisoformat(published_elem.text)
                        published_timestamp = dt.timestamp()
                    except (ValueError, AttributeError):
                        pass

                # Get thumbnail URL
                thumbnail = None
                if thumbnail_elem is not None:
                    thumbnail = thumbnail_elem.get('url')

                # Extract author username (format: /u/username)
                author = ""
                if author_elem is not None and author_elem.text:
                    author = author_elem.text.replace('/u/', '')

                posts.append({
                    "title": title_elem.text,
                    "author": author,
                    "url": link_elem.get('href', ''),
                    "published": published_timestamp,
                    "thumbnail": thumbnail,
                })

            data = {
                "subreddit": subreddit,
                "timeframe": timeframe,
                "posts": posts,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }

            print(f"✅ Fetched {len(posts)} posts from r/{subreddit} (top/{timeframe})")
            return data

        except Exception as e:
            print(f"❌ Failed to fetch or parse r/{subreddit} RSS: {e}")
            raise

    def render(self, processed_data: Dict[str, Any]) -> str:
        """Render Reddit posts widget HTML."""
        subreddit = processed_data["subreddit"]
        timeframe = processed_data["timeframe"]
        posts = processed_data["posts"]
        timestamp_iso = processed_data["fetched_at"]

        return self.render_template(
            "widgets/reddit_posts.html",
            size=self.size,
            subreddit=subreddit,
            timeframe=timeframe,
            posts=posts,
            timestamp_iso=timestamp_iso
        )
