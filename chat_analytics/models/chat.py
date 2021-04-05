from typing import List, Union

from chat_analytics.models.message import Message


class Chat:
    def __init__(self, messages: Union[List[Message], None] = None):
        self.messages = [] if messages is None else messages

    def add_chat(self, chat):
        self.messages += chat.messages

    def add_message(self, message: Message):
        self.messages.append(message)

    def add_messages(self, messages: List[Message]):
        self.messages += messages
