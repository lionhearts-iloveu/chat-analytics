from collections import defaultdict, Counter
from datetime import date
from os.path import join, exists
from pickle import load, dump
from typing import Tuple, Dict, List, Set

import pandas as pd
from pandas import DataFrame

from chat_analytics.config.config import config
from chat_analytics.parsers.instagram import instagramParser
from chat_analytics.parsers.whatsapp import whatsappParser
from chat_analytics.utils.cache import apply_cache

PARSERS = [instagramParser, whatsappParser]


def analise_chat():
    df_topics, df_words = get_counts()
    for topic in config.topics:
        tmp = df_topics.groupby("#sender#")[topic.name].sum()
        print(topic.name, str(tmp))
    print(df_words.sum(numeric_only=True).sort_values(ascending=False)[0:50])


def get_counts() -> Tuple[DataFrame, DataFrame]:
    frames_topics = list()
    frames_words = list()
    for parser in PARSERS:
        chat = apply_cache(config.cache_chat, parser.name, parser.parse, [])
        frames_topics.append(apply_cache(config.cache_df_topics, parser.name, compute_counts_topics, [chat]))
        frames_words.append(apply_cache(config.cache_df_words, parser.name, compute_counts_words, [chat]))
    return pd.concat(frames_topics, axis=0).reset_index(), pd.concat(frames_words, axis=0).reset_index()


def compute_counts_topics(chat) -> DataFrame:
    return DataFrame(chat.get_count_per_topics(config.topics))


def compute_counts_words(chat) -> Dict[Tuple[str, date, str], Counter]:
    return DataFrame(chat.get_count())


def get_cached_path(parser_name):
    return join(config.cache_df, parser_name + ".pickle")