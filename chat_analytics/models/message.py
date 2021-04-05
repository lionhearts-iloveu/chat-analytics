from datetime import datetime


class Message:
    def __init__(self, sender: str = "", content: str = "", data_ms: datetime = None):
        self.sender = sender
        self.content = content
        self.date_ms = data_ms

    def add_content(self, content: str):
        self.content += content

    def normalize_content(self):
        # TODO
        pass
