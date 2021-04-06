from typing import List

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import unidecode


def stemming(string: str, lang: str = "english"):
    words = tokenize(string)
    return [SnowballStemmer(lang).stem(word) for word in words]


def tokenize(string: str) -> List[str]:
    normalized = normalize(string)
    return word_tokenize(normalized)


def normalize(string: str) -> str:
    return unidecode.unidecode(string).lower()

