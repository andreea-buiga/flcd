from hashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hashtable = HashTable()

    def add(self, symbol):
        return self.__hashtable.add(symbol)

    def search(self, symbol):
        return self.__hashtable.search_symbol(symbol)
