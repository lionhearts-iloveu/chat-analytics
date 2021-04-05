from typing import List, Dict

import yaml

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

    def load_topics(self, filename: str):
        with open(filename) as file:
            topics_yaml = yaml.load(file, Loader=yaml.SafeLoader)
        for topic_name, data in topics_yaml.items():
            self.topics.append(Topic(topic_name, data))

    def load_senders(self, filename: str):
        with open(filename) as file:
            self.senders = yaml.load(file, Loader=yaml.SafeLoader)

config = Config()