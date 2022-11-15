from FA import FA
from symbol_table import SymbolTable
from typing import List, Tuple
import re


class Scanner:
    def __init__(self, option):
        self.__symbol_table = SymbolTable(30)
        self.__pif: List[Tuple[str, int]] = []
        self.__option = option
        self.__FA_identifier = FA("./FA_input/FA_identifier.in")
        self.__FA_integer_constant = FA("./FA_input/FA_integer_constant.in")
        self.__message = ""
        self.__separators = ['(', ')', '[', ']', '{', '}', ';', ' ', '\n', '"', '&&', '||',
                             '+', '-', '*', '%', '/', '//', '=', '<', '>', '<=', '>=', '==']
        self.__keywords = ['int', 'bool', 'char', 'string', 'if', 'else', 'while', 'for', 'step',
                           'read', 'write', 'arr', 'hello', 'bye', 'BEGIN', 'END']

    def is_identifier(self, string):
        """
        check if the string is an identifier
        """
        # return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', string) is not None
        return self.__FA_identifier.check_sequence(string)

    def is_constant(self, string):
        """
        check if string is a constant
        """
        # int_check = re.search("0|[+-]?[1-9][0-9]*", string)
        # char_check = re.search("'[a-zA-Z0-9]'", string)
        # string_check = re.search('"[a-zA-Z0-9]*"', string)

        # return int_check is not None or char_check is not None or string_check is not None
        return self.__FA_integer_constant.check_sequence(string)

    @staticmethod
    def double_separators(sep1, sep2):
        """
        check for the special case with double separators
        """
        if (sep1 == '=' and sep2 == '=') or \
                (sep1 == '<' and sep2 == '=') or \
                (sep1 == '>' and sep2 == '=') or \
                (sep1 == '!' and sep2 == '=') or \
                (sep1 == '/' and sep2 == '/') or \
                (sep1 == '|' and sep2 == '|') or \
                (sep1 == '&' and sep2 == '&'):
            return True
        return False

    @staticmethod
    def read_from_file(file_name):
        file = open(file_name, 'r')
        return file.readlines()

    def write_to_file(self, file_name, option):
        with open(file_name, 'w') as file:
            if option == "ST":
                file.write("SymbolTable with hash table representation\n")
                file.write(str(self.__symbol_table))
            elif option == "PIF":
                for token, position_in_st in self.__pif:
                    file.write(f"{token} | {position_in_st}\n")

    def scan(self, file_name):
        """
        scanning algorithm
        """
        lines = self.read_from_file(file_name)
        number_of_line = 0
        self.__message = ""
        for line in lines:
            program_lines = []
            line_with_code = re.split('([^a-zA-Z0-9])', line)

            for element in line_with_code:
                if element != '\t' and element != '' and element != ' ' and element != '\n':
                    program_lines.append(element)
            number_of_line = number_of_line + 1
            i = 0
            while i < len(program_lines):
                token = program_lines[i]

                # check if it is separator or keyword
                if token in self.__separators or token in self.__keywords:
                    self.__pif.append((token, -1))
                # identifiers and constants
                elif self.is_identifier(token) or self.is_constant(token):
                    posInST = self.__symbol_table.add(token)
                    if self.is_constant(token):
                        self.__pif.append(('CONSTANT', posInST))
                    else:
                        self.__pif.append(('IDENTIFIER', posInST))
                # handle double separators (<=, >=, ==, !=, &&, ||)
                elif i < len(program_lines) - 1:
                    if self.double_separators(token, program_lines[i + 1]):
                        self.__pif.append((token + program_lines[i + 1], -1))
                    else:
                        self.__message += "Lexical error at line " + str(
                            number_of_line) + " unknown token " + token + program_lines[i + 1] + "\n"
                    i = i + 1
                else:
                    self.__message += "Lexical error at line " + str(number_of_line) + " unknown token " + token + "\n"
                i = i + 1

        if self.__message == "":
            self.write_to_files()
            self.__message = "Lexically correct! :)"

    def write_to_files(self):
        self.write_to_file(f'./ST/ST{self.__option}.out', "ST")
        self.write_to_file(f'./PIF/PIF{self.__option}.out', "PIF")

    def get_symbol_table(self):
        return self.__symbol_table

    def get_pif(self):
        return self.__pif

    def get_message(self):
        return self.__message

    def set_option(self, option):
        self.__option = option
