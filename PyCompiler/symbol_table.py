from pyc_parser import BinOp, Num


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, type_):
        self.symbols[name] = type_

    def lookup(self, name):
        return self.symbols.get(name)

class TypeChecker:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def check(self, node):
        if isinstance(node, BinOp):
            left_type = self.check(node.left)
            right_type = self.check(node.right)
            if left_type != right_type:
                raise TypeError(f'Type mismatch: {left_type} and {right_type}')
            return left_type
        elif isinstance(node, Num):
            return 'int' if '.' not in node.value else 'float'
        else:
            raise Exception('Unknown node')