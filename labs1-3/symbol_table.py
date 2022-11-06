from hash_table import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hashtable = HashTable(size)

    def add(self, symbol):
        """
        add element to the symbol table
        """
        return self.__hashtable.add(symbol)

    def search(self, symbol):
        """
        search symbol in symbol table
        """
        return self.__hashtable.search_symbol(symbol)

    def symbol(self, position):
        """
        get the symbol on position
        """
        return self.__hashtable.symbol(position)

    def size(self):
        return self.__hashtable.size()

    def __str__(self):
        st_str = ""
        for elem in range(self.size()):
            st_str += str(elem) + " -> " + str(self.symbol(elem)) + "\n"

        return st_str
