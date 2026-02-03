import requests


HN_API_URL = "https://hacker-news.firebaseio.com/v0"


def fetch_hacker_news(limit=5):
    """
    Fetch top Hacker News stories.
    Ensures EVERY item has a valid clickable link.
    """
    response = requests.get(f"{HN_API_URL}/topstories.json")
    response.raise_for_status()

    story_ids = response.json()[:limit]
    items = []

    for story_id in story_ids:
        story_resp = requests.get(f"{HN_API_URL}/item/{story_id}.json")
        story_resp.raise_for_status()
        story = story_resp.json()

        # ✅ CRITICAL FIX: guarantee a valid link
        link = story.get("url")
        if not link:
            link = f"https://news.ycombinator.com/item?id={story_id}"

        items.append({
            "title": story.get("title", "No title"),
            "content": story.get("text", ""),
            "link": link,
            "source": "Hacker News"
        })

    return items
