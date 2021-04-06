from datetime import datetime
from typing import Tuple

from bs4 import BeautifulSoup as Soup

from chat_analytics.config.config import config
from chat_analytics.models.chat import Chat
from chat_analytics.models.message import Message
from chat_analytics.parsers.parser import Parser


class InstagramParser(Parser):
    def __init__(self, folder):
        super().__init__(folder, "instagram")

    def parse_file(self, filename: str) -> Chat:
        chat = Chat()
        with open(filename) as file:
            soup = Soup(file, 'html.parser')
        for raw_msg in soup.find_all("div", {"class": "pam _3-95 _2ph- _2lej uiBoxWhite noborder"}):
            chat.add_message(Message(*self.extract_metadata(raw_msg)))
        return chat

    def extract_metadata(self, raw_msg: Soup) -> Tuple[str, str, datetime, str]:
        d = datetime.strptime(raw_msg.select_one('div[class="_3-94 _2lem"]').get_text(),
                              "%b %d, %Y, %I:%M %p")
        sender = raw_msg.select_one('div[class="_3-95 _2pim _2lek _2lel"]').get_text()
        content = raw_msg.select_one('div[class="_3-95 _2let"]>div>div:nth-child(2)').get_text()
        return sender, content, d, self.name


instagramParser = InstagramParser(config.instagram_folder)
