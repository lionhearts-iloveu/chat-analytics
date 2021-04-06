import re
from datetime import datetime
from typing import Tuple

from chat_analytics.config.config import config
from chat_analytics.models.chat import Chat
from chat_analytics.models.message import Message
from chat_analytics.parsers.parser import Parser


class WhatsappParser(Parser):
    name = "whatsApp"

    def __init__(self, folder):
        super().__init__(folder)

    def parse_file(self, filename: str) -> Chat:
        chat = Chat()
        with open(filename) as file:
            for line in file:
                if self._is_new_message(line):
                    message = Message(*self.extract_metadata(line))
                    chat.add_message(message)
                else:
                    message.add_content(line)
        return chat

    @staticmethod
    def extract_metadata(line: str) -> Tuple[str, str, datetime, str]:
        d = datetime.strptime(line[1:21], "%d/%m/%Y, %H:%M:%S")
        sender, content = line[22:].split(":", 1)
        return sender, content, d, WhatsappParser.name

    @staticmethod
    def _is_new_message(line: str) -> bool:
        return True if re.match(r"\[[0-9]{2}/[0-9]{2}/[0-9]{4}, [0-9]{2}:[0-9]{2}:[0-9]{2}]", line[:22]) else False


whatsappParser = WhatsappParser(config.whatsapp_folder)
