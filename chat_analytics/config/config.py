from pathlib import Path
from typing import List, Dict, Set

import yaml
from nltk.corpus import stopwords

from chat_analytics.models.topic import Topic


class Config:
    def __init__(self):
        self.topics: List[Topic] = []
        self.senders: Dict[str, str] = {}
        with open("./config/config.yaml") as file:
            parsed = yaml.load(file, Loader=yaml.SafeLoader)
        self.load_topics(parsed['topics'])
        self.load_senders(parsed['senders'])
        self.facebook_folder: str = parsed['facebook']
        self.instagram_folder: str = parsed['instagram']
        self.whatsapp_folder: str = parsed['whatsapp']
        self.cache_chat: str = parsed['cache_chat']
        self.cache_df_topics: str = parsed['cache_df_topics']
        self.cache_df_words: str = parsed['cache_df_words']
        self.stopwords: Set[str] = set()
        self.load_stopwords(parsed['stopwords'])
        self.mkdir_caches()

    def load_topics(self, filename: str):
        with open(filename) as file:
            topics_yaml = yaml.load(file, Loader=yaml.SafeLoader)
        for topic_name, data in topics_yaml.items():
            self.topics.append(Topic(topic_name, data))

    def load_senders(self, filename: str):
        with open(filename) as file:
            self.senders = yaml.load(file, Loader=yaml.SafeLoader)

    def mkdir_caches(self):
        Path(self.cache_chat).mkdir(parents=True, exist_ok=True)
        Path(self.cache_df_topics).mkdir(parents=True, exist_ok=True)
        Path(self.cache_df_words).mkdir(parents=True, exist_ok=True)

    def load_stopwords(self, filename: str):
        self.stopwords = set(list(stopwords.words('french'))
                             + list(stopwords.words('english')))
        with open(filename) as file:
            for word in file:
                self.stopwords.add(word.strip())

config = Config()
