from hash_table import HashTable
from identifier import Identifier


class SymbolTable:
    def __init__(self):
        self.table = HashTable()
        self.checkingTable = {}

    def add(self, new_entry):
        entry = self.checkingTable.get(new_entry.get_key())
        if entry is None:
            self.checkingTable[new_entry.get_key()] = new_entry.get_value()
            self.table.add(new_entry.get_key(), new_entry.get_value())
        else:
            if isinstance(new_entry, Identifier) and isinstance(entry, Identifier):
                self.table.add(new_entry.get_key(), new_entry.get_value())

    def get(self, key):
        return self.table.get(key)

    def print_symbol_table(self):
        for key in self.table.items():
            value = self.table.items()[key]
            print("{ ID:", value[0], ", Value:", value[1], "}")
