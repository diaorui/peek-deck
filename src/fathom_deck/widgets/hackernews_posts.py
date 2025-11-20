"""HackerNews posts widget using Algolia Search API."""

from datetime import datetime, timezone
from typing import Any, Dict, List

from ..core.base_widget import BaseWidget
from ..core.http_cache import get_http_client


class HackernewsPostsWidget(BaseWidget):
    """Displays recent posts from HackerNews search.

    Required params:
        - query: Search query (e.g., "bitcoin", "ai", "python")

    Optional params:
        - limit: Number of posts to show (default: 8)
        - min_points: Minimum points threshold for quality filter (default: 10)
        - sort_by: Sort order - "date" or "relevance" (default: "date")
    """

    def get_required_params(self) -> list[str]:
        return ["query"]

    def fetch_data(self) -> Dict[str, Any]:
        """Fetch recent posts from HackerNews."""
        self.validate_params()

        query = self.merged_params["query"]
        limit = self.merged_params.get("limit", 8)
        min_points = self.merged_params.get("min_points", 10)
        sort_by = self.merged_params.get("sort_by", "date")
        client = get_http_client()

        try:
            # Fetch posts from HackerNews Algolia API
            if sort_by == "relevance":
                base_url = "https://hn.algolia.com/api/v1/search"
            else:  # default to date
                base_url = "https://hn.algolia.com/api/v1/search_by_date"

            params = {
                "query": query,
                "tags": "story",
                "hitsPerPage": limit,
            }

            # Add numeric filter for minimum points
            if min_points > 0:
                params["numericFilters"] = f"points>{min_points}"

            headers = {
                "User-Agent": "fathom-deck/1.0.0"
            }
            hn_data = client.get(base_url, params=params, headers=headers, response_type="json")

            # Extract posts from HN API response
            posts = []
            for hit in hn_data["hits"]:
                posts.append({
                    "title": hit["title"],
                    "url": hit.get("url", f"https://news.ycombinator.com/item?id={hit['objectID']}"),
                    "hn_url": f"https://news.ycombinator.com/item?id={hit['objectID']}",
                    "author": hit["author"],
                    "points": hit["points"],
                    "num_comments": hit["num_comments"],
                    "created_at": hit["created_at"],
                    "object_id": hit["objectID"],
                })

            data = {
                "query": query,
                "sort_by": sort_by,
                "min_points": min_points,
                "posts": posts,
                "total_hits": hn_data["nbHits"],
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }

            print(f"✅ Fetched {len(posts)} HN posts for query '{query}'")
            return data

        except Exception as e:
            print(f"❌ Failed to fetch or parse HN posts for '{query}': {e}")
            raise

    def render(self, processed_data: Dict[str, Any]) -> str:
        """Render HackerNews posts widget HTML."""
        query = processed_data["query"]
        sort_by = processed_data["sort_by"]
        min_points = processed_data["min_points"]
        posts = processed_data["posts"]
        total_hits = processed_data["total_hits"]
        timestamp_iso = processed_data["fetched_at"]

        return self.render_template(
            "widgets/hackernews_posts.html",
            size=self.size,
            query=query,
            sort_by=sort_by,
            min_points=min_points,
            posts=posts,
            total_hits=total_hits,
            timestamp_iso=timestamp_iso
        )
