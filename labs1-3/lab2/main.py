import unittest

from symbolTable import SymbolTable


class SymbolTableTestCase(unittest.TestCase):
    def test_symbol_table(self):
        st = SymbolTable()
        st.add(5)
        self.assertEqual(st.search(5), 13)
        self.assertNotEqual(st.add(5), 13)
        self.assertEqual(st.add(5), -1)
        self.assertEqual(st.search(10), -1)
