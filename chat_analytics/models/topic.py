from typing import List


class Topic:
    def __init__(self, name: str, data: dict):
        self.name: str = name
        self.simple: List[str] = list(data["simple"]) if "simple" in data else []
        self.regex: List[str] = list(data["regex"]) if "regex" in data else []
        self.token: List[str] = list(data["token"]) if "token" in data else []
