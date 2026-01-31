import feedparser
from datetime import datetime

def fetch_product_news(limit=5):
    # Product Hunt RSS feed (public)
    feed_url = "https://www.producthunt.com/feed"
    feed = feedparser.parse(feed_url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({
            'title': entry.title,
            'link': entry.link,
            'content': entry.summary if hasattr(entry, 'summary') else '',
            'source': 'Product Hunt',
            'timestamp': datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else None
        })
    return items