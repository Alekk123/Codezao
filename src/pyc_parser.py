# Definição da classe base AST
class AST:
    pass

# Classes para diferentes tipos de nós na AST
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.value = token[1]

class VarDecl(AST):
    def __init__(self, var_type, var_name, value):
        self.var_type = var_type
        self.var_name = var_name
        self.value = value

class FuncDecl(AST):
    def __init__(self, return_type, func_name, body):
        self.return_type = return_type
        self.func_name = func_name
        self.body = body

class Print(AST):
    def __init__(self, text):
        self.text = text

# Definição do Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        if self.current_token() and self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise Exception(f'Error parsing input: Expected {token_type}, got {self.current_token()}')

    def factor(self):
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Num(token)
        elif token[0] == 'ID':
            self.eat('ID')
            return token[1]
        else:
            raise Exception('Invalid syntax')

    def term(self):
        node = self.factor()
        while self.current_token() and self.current_token()[0] in ('MUL', 'DIV'):
            token = self.current_token()
            self.eat(token[0])
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            token = self.current_token()
            self.eat(token[0])
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def variable_declaration(self):
        var_type = self.current_token()
        if var_type[0] in ('INT', 'FLOAT', 'CHAR'):
            self.eat(var_type[0])
            var_name = self.current_token()
            self.eat('ID')
            self.eat('ASSIGN')
            value = self.expr()
            self.eat('END')
            return VarDecl(var_type=var_type[1], var_name=var_name[1], value=value)
        else:
            raise Exception(f"Unexpected variable type {var_type}")

    def print_statement(self):
        self.eat('PRINT')
        self.eat('LPAREN')
        text = self.current_token()
        self.eat('STRING')
        self.eat('RPAREN')
        self.eat('END')
        return Print(text=text[1])

    def function_declaration(self):
        return_type = self.current_token()
        self.eat('INT')
        func_name = self.current_token()
        self.eat('MAIN')
        self.eat('LPAREN')
        self.eat('RPAREN')
        self.eat('LBRACE')

        body = []
        while self.current_token() and self.current_token()[0] != 'RBRACE':
            if self.current_token()[0] in ('INT', 'FLOAT', 'CHAR'):
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'PRINT':
                body.append(self.print_statement())
            elif self.current_token()[0] == 'RETURN':
                self.eat('RETURN')
                return_value = self.current_token()
                self.eat('NUMBER')
                body.append(return_value[1])
                self.eat('END')

        self.eat('RBRACE')
        return FuncDecl(return_type=return_type[1], func_name=func_name[1], body=body)

    def parse(self):
        return self.function_declaration()
