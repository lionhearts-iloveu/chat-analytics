from typing import List, Union

from chat_analytics.models.message import Message


class Chat:
    def __init__(self, messages: Union[List[Message], None] = None):
        self.messages = [] if messages is None else messages
