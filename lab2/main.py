from constant import Constant
from identifier import Identifier
from symbol_table import SymbolTable


def test_symbol_table():
    symbol_table = SymbolTable()

    v1 = Identifier('a', 5)
    v2 = Identifier('b', 9)
    v3 = Identifier('c', 12)
    v4 = Identifier('a', 14)
    c1 = Constant('d', 7)

    symbol_table.add(v1)
    symbol_table.add(v2)
    symbol_table.add(v3)
    symbol_table.add(c1)
    symbol_table.add(v4)

    v2.set_value(42)
    symbol_table.add(v2)

    c2 = Constant('d', 17)
    symbol_table.add(c2)

    symbol_table.print_symbol_table()


test_symbol_table()
