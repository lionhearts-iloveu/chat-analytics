from abc import ABC, abstractmethod
from os import listdir
from os.path import isfile, join
from typing import List

from chat_analytics.models.chat import Chat


class Parser(ABC):
    def __init__(self, folder):
        self.folder = folder

    def parse(self) -> Chat:
        chat = Chat()
        for filename in self.get_all_filenames():
            chat.add_chat(self.parse_file(filename))
        return chat

    @abstractmethod
    def parse_file(self, filename: str) -> Chat:
        pass

    def get_all_filenames(self) -> List[str]:
        return [join(self.folder, f) for f in listdir(self.folder) if isfile(join(self.folder, f))]
