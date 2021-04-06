from os.path import join, exists
from pickle import load, dump

import pandas as pd
from pandas import DataFrame

from chat_analytics.config.config import config
from chat_analytics.parsers.instagram import instagramParser
from chat_analytics.parsers.whatsapp import whatsappParser

PARSERS = [instagramParser, whatsappParser]


def analise_chat():
    df = compute_counts()
    for topic in config.topics:
        tmp = df.groupby("sender")[topic.name].sum()
        print(topic.name, str(tmp))


def compute_counts() -> DataFrame:
    frames = list()
    for parser in PARSERS:
        cached_path = get_cached_path(parser.name)
        if exists(cached_path):
            with open(cached_path, "rb") as cache:
                df = load(cache)
        else:
            chat = parser.parse()
            df = DataFrame(chat.get_count(config.topics))
            with open(cached_path, "wb") as cache:
                dump(df, cache)
        frames.append(df)
    return pd.concat(frames, axis=0).reset_index()


def get_cached_path(parser_name):
    return join(config.cache_df, parser_name + ".pickle")