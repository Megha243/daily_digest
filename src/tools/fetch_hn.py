import httpx
from datetime import datetime

# def fetch_hacker_news():
#     top_stories = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()[:3]  # Limit to 3
#     items = []
#     for story_id in top_stories:
#         url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
#         story = httpx.get(url).json()
#         if story and 'title' in story:
#             items.append({
#                 'title': story['title'],
#                 'content': story.get('text', ''),
#                 'source': 'Hacker News',
#                 'timestamp': datetime
# .fromtimestamp(story['time'])
#             })
#     return items
def fetch_hacker_news():
    top_stories = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()[:5]
    items = []
    for story_id in top_stories:
        url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
        story = httpx.get(url).json()
        if story and 'title' in story:
            link = story.get('url', f"https://news.ycombinator.com/item?id={story_id}")
            items.append({
                'title': story['title'],
                'link': link,
                'content': story.get('text', ''),
                'source': 'Hacker News',
                'timestamp': datetime.fromtimestamp(story['time'])
            })
    return items