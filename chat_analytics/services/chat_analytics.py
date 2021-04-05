from pandas import DataFrame

from chat_analytics.config.config import config
from chat_analytics.models.chat import Chat
from chat_analytics.parsers.whatsapp import whatsappParser


def analise_chat(chat: Chat):
    df = DataFrame(chat.get_count(config.topics))
    for topic in config.topics:
        tmp = df.groupby("sender")[topic.name].sum()
        print(topic.name, str(tmp))


def load_chat() -> Chat:
    chat = Chat()
    chat.add_chat(whatsappParser.parse())
    return chat
