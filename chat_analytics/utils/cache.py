from pickle import load, dump
from os.path import join, exists


def apply_cache(folder: str, filename: str, compute_function, args):
    cached_path = get_cached_path(folder, filename)
    if exists(cached_path):
        with open(cached_path, "rb") as cache:
            res = load(cache)
    else:
        res = compute_function(*args)
        with open(cached_path, "wb") as cache:
            dump(res, cache)
    return res


def get_cached_path(folder, filename):
    return join(folder, filename.split('.')[0] + ".pickle")