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

class Input:
    def __init__(self, var_name):
        self.var_name = var_name

class FunctionCall:
    def __init__(self, func_name):
        self.func_name = func_name
        
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

    # def variable_declaration(self):
    #     var_type = self.current_token()
    #     if var_type[0] in ('INT', 'FLOAT', 'CHAR'):
    #         self.eat(var_type[0])
    #         var_name = self.current_token()
    #         self.eat('ID')
    #         self.eat('ASSIGN')
    #         value = self.expr()
    #         self.eat('END')
    #         return VarDecl(var_type=var_type[1], var_name=var_name[1], value=value)
    #     else:
    #         raise Exception(f"Unexpected variable type {var_type}")
    def variable_declaration(self):
        var_type = self.current_token()  # Tipo da variável
        self.eat('INT')  # Consome 'SeViraNos30'
        var_name = self.current_token()  # Nome da variável
        self.eat('ID')  # Consome o nome da variável
    
        # Verificar se há uma atribuição inicial (inicialização da variável)
        value = None
        if self.current_token()[0] == 'ASSIGN':  # Verifica se há um '=' após a variável
            self.eat('ASSIGN')
            value = self.current_token()
            self.eat('NUMBER')  # Espera um valor numérico após '='
    
        self.eat('END')  # Espera um ';'
    
        return VarDecl(var_type=var_type[1], var_name=var_name[1], value=value[1] if value else None)

    def print_statement(self):
        self.eat('PRINT')
        self.eat('LPAREN')
    
        # Verifica se é uma string ou um identificador
        if self.current_token()[0] == 'STRING':
            text = self.current_token()
            self.eat('STRING')
        elif self.current_token()[0] == 'ID':  # Caso de impressão de uma variável (ID)
            text = self.current_token()
            self.eat('ID')
        else:
            raise Exception(f'Error parsing input: Expected STRING or ID, got {self.current_token()}')
    
        self.eat('RPAREN')
        self.eat('END')
    
        return Print(text=text[1])
    
    def input_statement(self):  # Adiciona suporte para Receba()
        self.eat('INPUT')
        self.eat('LPAREN')
        var_name = self.current_token()  # Nome da variável que receberá o input
        self.eat('ID')
        self.eat('RPAREN')
        self.eat('END')
        return Input(var_name=var_name[1])

    def function_declaration(self):
        return_type = self.current_token()  # Tipo de retorno da função
        self.eat('INT')  # Consome 'SeViraNos30'
        func_name = self.current_token()  # Nome da função
        self.eat('ID')
        self.eat('LPAREN')  # Consome '('
        self.eat('RPAREN')  # Consome ')'
        self.eat('LBRACE')  # Consome '{'

        # Corpo da função
        body = []
        while self.current_token() and self.current_token()[0] != 'RBRACE':
            if self.current_token()[0] == 'INT':
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'PRINT':
                body.append(self.print_statement())
            elif self.current_token()[0] == 'INPUT':
                body.append(self.input_statement())
            elif self.current_token()[0] == 'RETURN':
                body.append(self.return_statement())
            else:
                raise Exception(f"Unexpected token {self.current_token()} in function body")
        
        self.eat('RBRACE')  # Consome '}'
        return FuncDecl(return_type=return_type[1], func_name=func_name[1], body=body)
    
    def return_statement(self):
        self.eat('RETURN')  # Consome 'BeijoDoGordo'
        return_value = self.current_token()  # Valor a ser retornado (no caso, '0')
        self.eat('NUMBER')  # Consome o número
        self.eat('END')  # Consome ';'
        return return_value[1]  # Retorna o valor numérico

    def function_call(self):
        func_name = self.current_token()
        self.eat('ID')  # Consome o identificador da função
        self.eat('LPAREN')  # Consome o '('
        self.eat('RPAREN')  # Consome o ')'
        self.eat('END')  # Consome o ';'
        return FunctionCall(func_name=func_name[1])

    def parse(self):
        token = self.current_token()
        if token and token[0] == 'INT':
            # Distinguindo entre declaração de variável e função
            next_token = self.tokens[self.pos + 1]
            if next_token[0] == 'ID' and self.tokens[self.pos + 2][0] == 'LPAREN':
                return self.function_declaration()
            else:
                return self.variable_declaration()
        else:
            raise Exception(f"Unexpected token {token}")
