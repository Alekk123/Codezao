class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.value = token[1]

class VarDecl(AST):
    def __init__(self, var_type, var_name, value=None):
        self.var_type = var_type
        self.var_name = var_name
        self.value = value

class FuncDecl(AST):
    def __init__(self, return_type, func_name, body):
        self.return_type = return_type
        self.func_name = func_name
        self.body = body

class Output(AST):
    def __init__(self, text):
        self.text = text

class Input(AST):
    def __init__(self, var_name):
        self.var_name = var_name

class If(AST):
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class While(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class For(AST):
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body

class Break(AST):
    def __init__(self):
        pass

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
            var_name = token[1]
            self.eat('ID')
            return var_name
        else:
            raise Exception('Invalid syntax')

    def term(self):
        node = self.factor()
        while self.current_token() and self.current_token()[0] == 'OP':
            token = self.current_token()
            self.eat(token[0])
            node = BinOp(left=node, op=token[1], right=self.factor())
        return node

    def expr(self):
        return self.term()

    def variable_declaration(self):
        var_type = self.current_token()
        if var_type[0] in ('INT', 'FLOAT', 'CHAR', 'BOOLEAN'):
            self.eat(var_type[0])
            var_name = self.current_token()
            self.eat('ID')
            value = None
            if self.current_token() and self.current_token()[0] == 'ASSIGN':
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
        if text[0] == 'STRING':
            self.eat('STRING')
            output = Output(text=text[1])
        else:
            var_name = self.current_token()
            self.eat('ID')
            output = Output(text=var_name)
        self.eat('RPAREN')
        self.eat('END')
        return output

    def input_statement(self):
        self.eat('SCANF')
        self.eat('LPAREN')
        var_name = self.current_token()
        self.eat('ID')
        self.eat('RPAREN')
        self.eat('END')
        return Input(var_name=var_name[1])

    def if_statement(self):
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')
        self.eat('LBRACE')
        then_body = self.block()
        else_body = None
        if self.current_token() and self.current_token()[0] == 'ELSEIF':
            self.eat('ELSEIF')
            else_body = self.if_statement()
        elif self.current_token() and self.current_token()[0] == 'ELSE':
            self.eat('ELSE')
            self.eat('LBRACE')
            else_body = self.block()
        return If(condition, then_body, else_body)

    def while_statement(self):
        self.eat('WHILE')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = self.block()
        return While(condition, body)

    def for_statement(self):
        self.eat('FOR')
        self.eat('LPAREN')
        init = self.variable_declaration()
        condition = self.expr()
        self.eat('END')
        increment = self.expr()
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = self.block()
        return For(init, condition, increment, body)

    def break_statement(self):
        self.eat('BREAK')
        self.eat('END')
        return Break()

    def block(self):
        body = []
        while self.current_token() and self.current_token()[0] != 'RBRACE':
            if self.current_token()[0] in ('INT', 'FLOAT', 'CHAR', 'BOOLEAN'):
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'PRINT':
                body.append(self.print_statement())
            elif self.current_token()[0] == 'SCANF':
                body.append(self.input_statement())
            elif self.current_token()[0] == 'IF':
                body.append(self.if_statement())
            elif self.current_token()[0] == 'WHILE':
                body.append(self.while_statement())
            elif self.current_token()[0] == 'FOR':
                body.append(self.for_statement())
            elif self.current_token()[0] == 'BREAK':
                body.append(self.break_statement())
            elif self.current_token()[0] == 'RETURN':
                self.eat('RETURN')
                return_value = self.expr()
                body.append(Num(('NUMBER', return_value)))
                self.eat('END')
            else:
                raise Exception(f'Unexpected token in block: {self.current_token()}')
        self.eat('RBRACE')
        return body

    def function_declaration(self):
        self.eat('FUNCTION')
        self.eat('MAIN')
        self.eat('LPAREN')
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = self.block()
        return FuncDecl(return_type='int', func_name='main', body=body)

    def parse(self):
        return self.function_declaration()
