import re
from datetime import datetime
from typing import List, Union

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import unidecode

from chat_analytics.config.config import config
from chat_analytics.models.topic import Topic

nltk.download('punkt')


class Message:
    def __init__(self, sender: str = "", content: str = "", data_ms: datetime = None):
        self.sender = self.map_sender(sender)
        self.content = content
        self.normalized_content: str = self.normalize(content)
        self.en_content: List[str] = self.tokenize(content, "english")
        self.fr_content: List[str] = self.tokenize(content, "french")
        self.date_ms: datetime = data_ms

    def add_content(self, content: str):
        self.content += content
        self.normalized_content += self.normalize(content)
        self.en_content += self.tokenize(content, "english")
        self.fr_content += self.tokenize(content, "french")

    def count(self, topic: Topic):
        count = 0
        for regex in topic.regex:
            count += self.count_regex(regex)
        for simple in topic.simple:
            count += self.count_simple(simple)
        for token in topic.token:
            count += self.count_token(token)
        return count

    def count_token(self, substring: str) -> int:
        return max(self.count_match(self.tokenize(substring, "english"), self.en_content),
                   self.count_match(self.tokenize(substring, "french"), self.fr_content))

    def count_simple(self, substring: str) -> int:
        return self.content.count(substring)

    def count_regex(self, substring: str) -> int:
        return len(re.findall(substring, self.normalized_content))

    @staticmethod
    def map_sender(sender: str):
        for k in config.senders:
            if k in sender.lower():
                return config.senders[k]
        return sender

    @staticmethod
    def normalize(string: str) -> str:
        return unidecode.unidecode(string).lower()

    @staticmethod
    def tokenize(string: str, lang: str = "english") -> List[str]:
        normalized = Message.normalize(string)
        words = word_tokenize(normalized)
        return [SnowballStemmer(lang).stem(word) for word in words]

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
