from datetime import datetime
from json import load
from typing import Tuple

from chat_analytics.config.config import config
from chat_analytics.models.chat import Chat
from chat_analytics.models.message import Message
from chat_analytics.parsers.parser import Parser


class FacebookParser(Parser):
    def __init__(self, folder):
        super().__init__(folder, "facebook")

    def parse_file(self, filename: str) -> Chat:
        chat = Chat()
        with open(filename) as file:
            data = load(file)
        for raw_msg in data["messages"]:
            if "content" in raw_msg:
                chat.add_message(Message(*self.extract_metadata(raw_msg)))
        return chat

    def extract_metadata(self, raw_msg: dict) -> Tuple[str, str, datetime, str]:
        d = datetime.fromtimestamp(raw_msg["timestamp_ms"]/1000.0)
        sender = raw_msg["sender_name"]
        content = raw_msg["content"]
        return sender, content, d, self.name


facebookParser = FacebookParser(config.facebook_folder)
