from typing import List, Union


class Topic:
    def __init__(self, name: str, data: dict):
        self.name: str = name
        self.simple: List[str] = self.to_list(data["simple"]) if "simple" in data else []
        self.regex: List[str] = self.to_list(data["regex"]) if "regex" in data else []
        self.token: List[str] = self.to_list(data["token"]) if "token" in data else []

    @staticmethod
    def to_list(data: Union[str, list]):
        return data if isinstance(data, list) else [data]