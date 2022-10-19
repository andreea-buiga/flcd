import hashlib


class HashTable:
    def __init__(self):
        self.__items = {}

    def add(self, key, value):
        hashed_key = str(int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8))
        self.__items[hashed_key] = (key, value)

    def get(self, key):
        hashed_key = str(int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8))
        return self.__items[hashed_key]

    def items(self):
        return self.__items
