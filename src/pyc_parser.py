# Definição da classe base AST
class AST:
    pass

# Classes para diferentes tipos de nós na AST
class BinOp(AST):
    def __init__(self, left, op, right):
        """Define uma operação binária com operandos esquerdo e direito."""
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        """Representa um número na AST."""
        self.value = token[1]

class VarDecl(AST):
    def __init__(self, var_type, var_name, value):
        """Declaração de variável na AST."""
        self.var_type = var_type
        self.var_name = var_name
        self.value = value

class FuncDecl(AST):
    def __init__(self, return_type, func_name, body):
        """Declaração de função na AST."""
        self.return_type = return_type
        self.func_name = func_name
        self.body = body

class Print(AST):
    def __init__(self, text):
        """Instrução de impressão na AST."""
        self.text = text

class Input:
    def __init__(self, var_name):
        """Instrução de entrada (input) na AST."""
        self.var_name = var_name

class FunctionCall:
    def __init__(self, func_name):
        """Chamada de função na AST."""
        self.func_name = func_name

# Definição do Parser
class Parser:
    def __init__(self, tokens):
        """Inicializa o Parser com uma lista de tokens."""
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        """Retorna o token atual."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        """Verifica e consome o token esperado."""
        if self.current_token() and self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise Exception(f'Error parsing input: Expected {token_type}, got {self.current_token()}')

    # Parsing de expressões e termos
    def factor(self):
        """Faz o parsing de um fator (número ou variável)."""
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
        """Faz o parsing de um termo, lidando com multiplicação e divisão."""
        node = self.factor()
        while self.current_token() and self.current_token()[0] in ('MUL', 'DIV'):
            token = self.current_token()
            self.eat(token[0])
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        """Faz o parsing de uma expressão aritmética usando operadores aritméticos."""
        node = self.term()  # Inicializa com um termo para adição e subtração

        # Processa operadores aritméticos
        while self.current_token() and self.current_token()[0] == 'OP':
            token = self.current_token()
            self.eat('OP')
            node = BinOp(left=node, op=token[1], right=self.term())

        return node

    
    def comparison_expr(self):
        """Faz o parsing de uma expressão de comparação usando operadores como <, >, <=, >=, ==, !=."""
        node = self.logical_expr()  # Baseia-se em uma expressão lógica para compor a comparação

        # Processa operadores de comparação
        while self.current_token() and self.current_token()[0] == 'COMPARISON_OP':
            token = self.current_token()
            self.eat('COMPARISON_OP')
            node = BinOp(left=node, op=token[1], right=self.logical_expr())

        return node
    
    def logical_expr(self):
        """Faz o parsing de uma expressão lógica usando operadores lógicos como && e ||."""
        node = self.expr()  # Começa a expressão lógica com uma expressão aritmética ou comparativa

        # Processa operadores lógicos
        while self.current_token() and self.current_token()[0] == 'LOGICAL_OP':
            token = self.current_token()
            self.eat('LOGICAL_OP')
            node = BinOp(left=node, op=token[1], right=self.expr())

        return node
    
    def assignment_statement(self):
        """Processa uma declaração de atribuição."""
        var_name = self.current_token()
        self.eat('ID')
        self.eat('ASSIGN')

        # Processa a expressão do lado direito da atribuição
        expr = self.comparison_expr()  # Chama comparison_expr para avaliar completamente

        self.eat('END')
        return BinOp(left=var_name[1], op='=', right=expr)



    # Parsing de declaração de variável
    def variable_declaration(self):
        """Faz o parsing de uma declaração de variável."""
        var_type = self.current_token()  # Tipo da variável
        
        # Suporte para int, float, boolean e char
        if var_type[0] == 'INT':
            self.eat('INT')
        elif var_type[0] == 'FLOAT':
            self.eat('FLOAT')
        elif var_type[0] == 'BOOLEAN':
            self.eat('BOOLEAN')
        elif var_type[0] == 'CHAR':  # Suporte para char (Maoee)
            self.eat('CHAR')
        
        var_name = self.current_token()  # Nome da variável
        self.eat('ID')
    
        # Verifica se há uma atribuição inicial
        value = None
        if self.current_token()[0] == 'ASSIGN':
            self.eat('ASSIGN')
            if var_type[0] == 'CHAR':  # Para char, espera uma string de um único caractere
                value = self.current_token()
                self.eat('STRING')  # Espera uma string
            else:
                value = self.current_token()
                self.eat('NUMBER')  # Espera um número
    
        self.eat('END')  # Consome ';'
    
        return VarDecl(var_type=var_type[1], var_name=var_name[1], value=value[1] if value else None)

    # Parsing da instrução de impressão (PoeNaTela)
    def print_statement(self):
        """Faz o parsing de uma instrução de impressão (PoeNaTela)."""
        self.eat('PRINT')
        self.eat('LPAREN')
    
        # Verifica se é uma string ou variável (ID)
        if self.current_token()[0] == 'STRING':
            text = self.current_token()
            self.eat('STRING')
        elif self.current_token()[0] == 'ID':
            text = self.current_token()
            self.eat('ID')
        else:
            raise Exception(f'Error parsing input: Expected STRING or ID, got {self.current_token()}')
    
        self.eat('RPAREN')
        self.eat('END')
    
        return Print(text=text[1])

    # Parsing da instrução de entrada (Receba)
    def input_statement(self):
        """Faz o parsing de uma instrução de entrada (Receba)."""
        self.eat('INPUT')
        self.eat('LPAREN')
        var_name = self.current_token()
        self.eat('ID')
        self.eat('RPAREN')
        self.eat('END')
        return Input(var_name=var_name[1])

    # Parsing de funções
    def function_declaration(self):
        """Faz o parsing de uma declaração de função."""
        return_type = self.current_token()  # Tipo de retorno da função
        self.eat('INT')  # Consome 'SeViraNos30' como tipo de retorno da função
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
            elif self.current_token()[0] == 'FLOAT':  # Suporte para float
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'BOOLEAN':  # Suporte para boolean
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'CHAR':  # Suporte para char (Maoee)
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'PRINT':
                body.append(self.print_statement())
            elif self.current_token()[0] == 'INPUT':
                body.append(self.input_statement())
            elif self.current_token()[0] == 'ID':
                body.append(self.assignment_statement())  # Aqui processamos as atribuições
            elif self.current_token()[0] == 'RETURN':
                body.append(self.return_statement())
            else:
                raise Exception(f"Unexpected token {self.current_token()} in function body")
        
        self.eat('RBRACE')  # Consome '}'
        return FuncDecl(return_type=return_type[1], func_name=func_name[1], body=body)

    # Parsing da instrução de retorno
    def return_statement(self):
        """Faz o parsing de uma instrução de retorno (BeijoDoGordo)."""
        self.eat('RETURN')
        return_value = self.current_token()
        self.eat('NUMBER')
        self.eat('END')
        return return_value[1]

    # Parsing de chamada de função
    def function_call(self):
        """Faz o parsing de uma chamada de função."""
        func_name = self.current_token()
        self.eat('ID')
        self.eat('LPAREN')
        self.eat('RPAREN')
        self.eat('END')
        return FunctionCall(func_name=func_name[1])

    def parse(self):
        """Função principal que inicia o parsing."""
        token = self.current_token()
        if token and token[0] == 'INT':
            next_token = self.tokens[self.pos + 1]
            if next_token[0] == 'ID' and self.tokens[self.pos + 2][0] == 'LPAREN':
                return self.function_declaration()
            else:
                return self.variable_declaration()
        else:
            raise Exception(f"Unexpected token {token}")