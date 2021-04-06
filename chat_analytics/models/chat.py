from collections import defaultdict, Counter
from datetime import date
from typing import List, Union, Dict, Tuple, Set

from nltk.chat import Chat

from chat_analytics.models.message import Message
from chat_analytics.models.topic import Topic


class Chat:
    def __init__(self, messages: Union[List[Message], None] = None):
        self.messages: List[Message] = [] if messages is None else messages

    def add_chat(self, chat) -> None:
        self.messages += chat.messages

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def add_messages(self, messages: List[Message]) -> None:
        self.messages += messages

    def get_count_per_topics(self, topics: List[Topic]) -> dict:
        data = defaultdict(list)
        for msg in self.messages:
            data["#sender#"].append(msg.sender)
            data["#datetime#"].append(msg.get_datetime())
            data["#app#"].append(msg.app)
            for topic in topics:
                data[topic.name].append(msg.count_for(topic))
        return data

    def get_count(self) -> Dict[str, list]:
        tmp: Dict[Tuple[str, date, str], Counter] = defaultdict(lambda: Counter())
        all_words: Set[str] = set()
        for msg in self.messages:
            count_words = msg.count_words()
            all_words.update(count_words.keys())
            tmp[(msg.sender, msg.get_date(), msg.app)].update(count_words)

        data: Dict[str, list] = defaultdict(list)

        for key in tmp.keys():
            sender, d, app = key
            data["#sender#"].append(sender)
            data["#date#"].append(d)
            data["#app#"].append(app)
            for word in all_words:
                data[word].append(tmp[key][word])
        return data

