from symbol_table import SymbolTable
from typing import List, Tuple
import re
from enum import Enum


class TypeOfToken(Enum):
    IDENTIFIER = 1
    CONSTANT = 2


class Scanner:
    def __init__(self, option):
        self.__symbol_table = SymbolTable(30)
        self.__pif: List[Tuple[str, int]] = []
        self.__option = option
        self.__message = ""
        self.__separators = ['(', ')', '[', ']', '{', '}', ';', ' ', '\n', '"', '&&', '||',
                             '+', '-', '*', '%', '/', '//', '=', '<', '>', '<=', '>=', '==']
        self.__keywords = ['int', 'bool', 'char', 'string', 'if', 'else', 'while', 'for', 'step',
                           'read', 'write', 'arr', 'hello', 'bye', 'BEGIN', 'END']

    @staticmethod
    def is_identifier(string):
        """
        check if the string is an identifier
        """
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', string) is not None

    @staticmethod
    def is_constant(string):
        """
        check if string is a constant
        """
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^(0|[+-]?[1-9][0-9]*),[0-9]*|^`.`$|^`.*`$', string) is not None

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
            string_constant = re.findall('"([^"]*)"', line)

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
                elif self.is_constant(token) or self.is_identifier(token):
                    # string constant
                    if len(string_constant) != 0 and token in string_constant[0]:
                        position_in_st = self.__symbol_table.add(string_constant)
                        self.__pif.append(('CONSTANT', position_in_st))
                    # identifier
                    elif self.is_identifier(token):
                        position_in_st = self.__symbol_table.add(token)
                        self.__pif.append(('IDENTIFIER', position_in_st))
                    # number constant
                    else:
                        position_in_st = self.__symbol_table.add(token)
                        self.__pif.append(('CONSTANT', position_in_st))
                # handle double separators (<=, >=, ==, !=, &&, ||)
                elif i < len(program_lines) - 1:
                    if self.double_separators(token, program_lines[i + 1]):
                        self.__pif.append((token + program_lines[i + 1], -1))
                        i = i + 1
                else:
                    self.__message += "Lexical error at line " + str(number_of_line) + " unknown token " + token + "\n"
                i = i + 1

        if self.__message == "":
            self.write_to_files()
            self.__message = "Lexically correct! :)"

    def write_to_files(self):
        self.write_to_file(f'./ST{self.__option}.out', "ST")
        self.write_to_file(f'./PIF{self.__option}.out', "PIF")

    def get_symbol_table(self):
        return self.__symbol_table

    def get_pif(self):
        return self.__pif

    def get_message(self):
        return self.__message

    def set_option(self, option):
        self.__option = option
