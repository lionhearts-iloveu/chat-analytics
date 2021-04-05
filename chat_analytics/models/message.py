from datetime import datetime


class Message:
    def __init__(self, sender: str, content: str, data_ms: datetime):
        self.sender = sender
        # TODO normalize content
        self.content = content
        self.date_ms = data_ms
