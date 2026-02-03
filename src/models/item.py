# class Item:
#     def __init__(self, title, link, content, source, timestamp):
#         self.title = title
#         self.link = link
#         self.content = content
#         self.source = source
#         self.timestamp = timestamp

from dataclasses import dataclass


@dataclass
class Item:
    title: str
    source: str
    link: str
    summary: str
