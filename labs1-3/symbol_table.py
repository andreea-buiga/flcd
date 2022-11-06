from hash_table import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hashtable = HashTable(size)

    def __str__(self):
        return str(self.__hashtable)

    def add(self, key):
        return self.__hashtable.add(key)

    def contains(self, key):
        return self.__hashtable.contains(key)

    def remove(self, key):
        self.__hashtable.remove(key)

    def get_position(self, key):
        return self.__hashtable.get_position(key)
