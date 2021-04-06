from typing import List, Union

from chat_analytics.utils.stemmer import stemming


class Topic:
    def __init__(self, name: str, data: dict):
        self.name: str = name
        self.simple: List[str] = self.to_list(data["simple"]) if "simple" in data else []
        self.regex: List[str] = self.to_list(data["regex"]) if "regex" in data else []
        self.token: List[str] = self.to_list(data["token"]) if "token" in data else []
        self.token_fr: List[List[str]] = list()
        self.token_en: List[List[str]] = list()
        self.stem_tokens()

    def stem_tokens(self) -> None:
        for token in self.token:
            self.token_en.append(stemming(token, "english"))
            self.token_fr.append(stemming(token, "french"))

    @staticmethod
    def to_list(data: Union[str, list]) -> List[str]:
        return data if isinstance(data, list) else [data]

