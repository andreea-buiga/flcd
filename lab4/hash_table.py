from collections import deque


class HashTable:
    def __init__(self, size):
        self.__size = size
        # deque ( implemented as a double ended linked list)
        # if two elements hash to the same value they are chained
        # to it's respective deque
        self.__items = [deque() for _ in range(size)]

    def hash(self, key):
        """
        h(k) = k % size - in our case k is the sum of ascii numbers
        :param key: input token
        :return: the value of the hash function
        """
        total_sum = 0
        for character in key:
            total_sum += ord(character)
        return total_sum % self.__size

    def add(self, key):
        if self.contains(key):
            return self.get_position(key)
        self.__items[self.hash(key)].append(key)
        return self.get_position(key)

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self) -> str:
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "-" + str(self.__items[i]) + "\n"
        return result

    def get_position(self, key):
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return listPosition, listIndex