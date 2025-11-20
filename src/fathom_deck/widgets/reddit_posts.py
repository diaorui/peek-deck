"""Reddit posts widget using Reddit JSON API."""

from datetime import datetime, timezone
from typing import Any, Dict, List

from ..core.base_widget import BaseWidget
from ..core.http_cache import get_http_client


class RedditPostsWidget(BaseWidget):
    """Displays recent posts from a subreddit.

    Required params:
        - subreddit: Subreddit name (e.g., "bitcoin", "cryptocurrency")

    Optional params:
        - limit: Number of posts to show (default: 5)
        - sort: Sort order - "hot", "new", "top", "rising" (default: "hot")
    """

    def get_required_params(self) -> list[str]:
        return ["subreddit"]

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch recent posts from subreddit."""
        self.validate_params()

        subreddit = self.merged_params["subreddit"]
        limit = self.merged_params.get("limit", 5)
        sort = self.merged_params.get("sort", "hot")
        client = get_http_client()

        try:
            # Fetch posts from Reddit JSON API
            url = f"https://www.reddit.com/r/{subreddit}/{sort}/.json"
            params = {"limit": limit}
            headers = {
                "User-Agent": "python:fathom-deck:v1.0.0 (by /u/fathom-deck-bot)"
            }
            reddit_data = client.get(url, params=params, headers=headers, response_type="json")

            # Extract posts from Reddit API response
            posts = []
            for child in reddit_data["data"]["children"]:
                post_data = child["data"]

                # Handle thumbnail - can be URL, "self", "default", or missing
                thumbnail = post_data.get("thumbnail", "")
                if not thumbnail.startswith("http"):
                    thumbnail = None

                posts.append({
                    "title": post_data["title"],
                    "author": post_data["author"],
                    "score": post_data["score"],
                    "num_comments": post_data["num_comments"],
                    "url": f"https://www.reddit.com{post_data['permalink']}",
                    "created_utc": post_data["created_utc"],
                    "is_self": post_data["is_self"],
                    "thumbnail": thumbnail,
                })

            data = {
                "subreddit": subreddit,
                "sort": sort,
                "posts": posts,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }

            print(f"✅ Fetched {len(posts)} posts from r/{subreddit}")
            return data

        except Exception as e:
            print(f"❌ Failed to fetch or parse r/{subreddit}: {e}")
            raise

    def render(self, processed_data: Dict[str, Any]) -> str:
        """Render Reddit posts widget HTML."""
        subreddit = processed_data["subreddit"]
        sort = processed_data["sort"]
        posts = processed_data["posts"]
        timestamp_iso = processed_data["fetched_at"]

        return self.render_template(
            "widgets/reddit_posts.html",
            size=self.size,
            subreddit=subreddit,
            sort=sort,
            posts=posts,
            timestamp_iso=timestamp_iso
        )
