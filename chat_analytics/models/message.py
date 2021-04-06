import re
from collections import Counter
from datetime import datetime
from typing import List, Union

from chat_analytics.config.config import config
from chat_analytics.models.topic import Topic
from chat_analytics.utils.stemmer import normalize, stemming


class Message:
    def __init__(self, sender: str = "", content: str = "", data_ms: datetime = None, app: str = ""):
        self.sender = self.map_sender(sender)
        self.content = content
        self.normalized_content: str = normalize(content)
        self.en_content: List[str] = stemming(content, "english")
        self.fr_content: List[str] = stemming(content, "french")
        self.date_ms: datetime = data_ms
        self.app = app

    def add_content(self, content: str) -> None:
        self.content += content
        self.normalized_content += normalize(content)
        self.en_content += stemming(content, "english")
        self.fr_content += stemming(content, "french")

    def count_for(self, topic: Topic) -> int:
        count = 0
        for regex in topic.regex:
            count += self.count_regex(regex)
        for simple in topic.simple:
            count += self.count_simple(simple)
        for i in range(len(topic.token)):
            count += self.count_token(topic.token_en[i], topic.token_fr[i])
        return count

    def count_words(self) -> Counter:
        pass

    def count_token(self, token_en: List[str], token_fr:  List[str]) -> int:
        return max(self.count_match(token_en, self.en_content),
                   self.count_match(token_fr, self.fr_content))

    def count_simple(self, substring: str) -> int:
        return self.content.count(substring)

    def count_regex(self, substring: str) -> int:
        return len(re.findall(substring, self.normalized_content))

    @staticmethod
    def map_sender(sender: str) -> str:
        for k in config.senders:
            if k in sender.lower():
                return config.senders[k]
        return sender

    @staticmethod
    def count_match(phrase: List[str], text: List[str]) -> int:
        count = 0
        if not text:
            return 0
        for i in range(len(text) - len(phrase) + 1):
            if Message.match(text[i], phrase[0]):
                is_phrase_match = True
                for j in range(1, len(phrase)):
                    if not Message.match(text[i + j], phrase[j]):
                        is_phrase_match = False
                        break
                if is_phrase_match:
                    count += 1
        return count

    @staticmethod
    def match(w1: str, w2: str) -> bool:
        # TODO allow typo
        return w1 == w2
