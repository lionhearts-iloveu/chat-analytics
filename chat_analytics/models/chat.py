from collections import defaultdict
from typing import List, Union

from chat_analytics.models.message import Message
from chat_analytics.models.topic import Topic


class Chat:
    def __init__(self, messages: Union[List[Message], None] = None):
        self.messages = [] if messages is None else messages

    def add_chat(self, chat):
        self.messages += chat.messages

    def add_message(self, message: Message):
        self.messages.append(message)

    def add_messages(self, messages: List[Message]):
        self.messages += messages

    def get_count(self, topics: List[Topic]) -> dict:
        data = defaultdict(list)
        for msg in self.messages:
            data["sender"].append(msg.sender)
            data["date_ms"].append(msg.date_ms)
            data["app"].append(msg.app)
            for topic in topics:
                data[topic.name].append(msg.count(topic))
        return data
