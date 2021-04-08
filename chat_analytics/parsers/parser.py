from abc import ABC, abstractmethod
from os import listdir
from os.path import isfile, join
from typing import List

from chat_analytics.config.config import config
from chat_analytics.models.chat import Chat


class Parser(ABC):
    def __init__(self, folder: str, name: str):
        self.folder: str = folder
        self.name: str = name

    def parse(self) -> Chat:
        chat = Chat()
        for filename in self.get_all_filenames():
            chat.add_chat(self.parse_file(join(self.folder, filename)))
        return chat

    @abstractmethod
    def parse_file(self, filename: str) -> Chat:
        pass

    @staticmethod
    def get_cached_path(filename) -> str:
        return join(config.cache_chat, filename.split('.')[0] + ".pickle")

    def get_all_filenames(self) -> List[str]:
        return [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
