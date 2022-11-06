class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__hashtable = {}
        for i in range(self.__size):
            self.__hashtable[i] = []

    def add(self, symbol):
        """
        :param symbol: symbol to be added to the hash table
        :return: position in the hashtable
        """
        position = self.search_symbol(symbol)
        if position == -1:
            hash_key = self.hash_function(symbol)
            self.__hashtable[hash_key].append(symbol)
            return hash_key

        return position

    def hash_function(self, symbol):
        """
        :param symbol: symbol to be hashed
        :return: the position - the sum of ascii numbers % size
        """
        ascii_sum = 0
        for i in range(len(str(symbol))):
            ascii_sum += ord(str(symbol)[i])

        return ascii_sum % self.__size

    def search_symbol(self, symbol):
        """
        :param symbol: symbol to be searched in the hash table
        :return: the position in hashtable if it is already there
                -1, otherwise
        """
        position = self.hash_function(symbol)
        if symbol not in self.__hashtable[position]:
            return -1

        return position

    def symbol(self, position):
        return self.__hashtable[position]

    def size(self):
        return self.__size
