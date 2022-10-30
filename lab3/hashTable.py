from functools import reduce


class HashTable:
    def __init__(self):
        self.__size = 20
        self.__hashtable = [[] for i in range(20)]

    def add(self, value):
        curr_hash = hash(value) % self.__size
        self.__hashtable[curr_hash].append(value)

    def __contains__(self, value):
        curr_hash = hash(value) % self.__size
        if value in self.__hashtable[curr_hash]:
            return True
        return False

    def clear(self):
        self.__hashtable = [[] for i in range(20)]

    @property
    def data(self):
        return reduce(lambda acc, curr: acc + curr, self.__hashtable, [])
