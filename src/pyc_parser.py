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
        
        # Define se a operação é uma comparação ou atribuição
        if op == '==':
            self.is_comparison = True
        elif op == '=':
            self.is_comparison = False
        else:
            self.is_comparison = None  # Outros operadores não são nem comparação nem atribuição

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
        
class IfNode(AST):
    def __init__(self, conditionals):
        """Inicializa um nó de condicional com todas as condições (if, elif, else). """
        self.conditionals = conditionals

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BreakNode(AST):
    """Representa uma instrução de interrupção de laço (break) na AST."""
    pass

class ForNode(AST):
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body

# Definição do Parser
class Parser:
    def __init__(self, tokens):
        """Inicializa o Parser com uma lista de tokens."""
        self.tokens = tokens
        self.pos = 0
        self.in_for_loop = False  # Controle para o modo `for`

    def current_token(self):
        """Retorna o token atual."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        """Verifica e consome o token esperado."""
        if self.current_token() and self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise Exception(f'Error parsing input: Expected {token_type}, got {self.current_token()}')

    def peek_next_token(self):
        """Visualiza o próximo token sem consumi-lo."""
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return None
    
     # Função principal para parsing de condicional
    def parse_conditional_statement(self):
        """Processa declarações condicionais (if, else if, else) na linguagem Codezão."""
        conditionals = []

        # Verificar 'EhUmaCiladaBino' para iniciar o bloco if
        if self.current_token() and self.current_token()[0] == 'IF':
            self.eat('IF')
            self.eat('LPAREN')
            condition = self.parse_expression()  # Avalia a expressão da condição if
            self.eat('RPAREN')
            self.eat('LBRACE')
            if_body = self.parse_body()  # Processa o corpo do bloco if
            self.eat('RBRACE')
            conditionals.append(('if', condition, if_body))

            # Verificar a existência de blocos else if (VoceEstaCertoDisso)
            while self.current_token() and self.current_token()[0] == 'ELSE_IF':
                self.eat('ELSE_IF')
                self.eat('LPAREN')
                condition = self.parse_expression()  # Avalia a expressão da condição else if
                self.eat('RPAREN')
                self.eat('LBRACE')
                elif_body = self.parse_body()  # Processa o corpo do bloco else if
                self.eat('RBRACE')
                conditionals.append(('elif', condition, elif_body))

            # Verificar a existência de bloco else (Errrou)
            if self.current_token() and self.current_token()[0] == 'ELSE':
                self.eat('ELSE')
                self.eat('LBRACE')
                else_body = self.parse_body()  # Processa o corpo do bloco else
                self.eat('RBRACE')
                conditionals.append(('else', else_body))

        return IfNode(conditionals)  # Retorna o nó if contendo todos os blocos
    
    def parse_while_statement(self):
        """Processa o laço `RodaARoda` e gera o nó WhileNode na AST."""
        self.eat('WHILE')
        self.eat('LPAREN')
        condition = self.parse_expression()  # Analisa a condição
        self.eat('RPAREN')
        self.eat('LBRACE')
        
        # Captura o corpo do `while`
        body = self.parse_body()
        
        self.eat('RBRACE')  # Fecha o bloco do `while`
        return WhileNode(condition, body)
    
    def parse_for_statement(self):
        """Processa o laço `VaiQueEhTua` e gera o nó ForNode na AST."""
        print("[DEBUG] Iniciando parsing do `for` (VaiQueEhTua)")
        self.eat('FOR')
        self.eat('LPAREN')
        
        # Ativa o modo `for`
        self.in_for_loop = True

        print("[DEBUG] Processando inicialização do `for`...")
        init = self.assignment_statement()
        print("[DEBUG] Inicialização do `for`:", init)

        print("[DEBUG] Processando condição do `for`...")
        condition = self.parse_expression()
        print("[DEBUG] Condição do `for`:", condition)

        # Consome `END` se presente após a condição no cabeçalho do `for`
        if self.current_token() and self.current_token()[0] == 'END':
            self.eat('END')

        print("[DEBUG] Processando incremento do `for`...")
        increment = self.assignment_statement()
        print("[DEBUG] Incremento do `for`:", increment)

        self.in_for_loop = False
        self.eat('RPAREN')  # Confirma fechamento do cabeçalho do `for`
        
        print("[DEBUG] Processando corpo do `for`...")
        self.eat('LBRACE')
        body = self.parse_body()
        self.eat('RBRACE')
        
        print("[DEBUG] Finalizando parsing do `for` com corpo:", body)
        return ForNode(init, condition, increment, body)
    
    # Parsing de expressões e termos
    def parse_expression(self):
        """Processa expressões gerais, incluindo comparações e lógicas."""
        node = self.parse_logical_expr()
        return node

    def parse_logical_expr(self):
        """Processa operadores lógicos (`&&`, `||`) e gerencia precedência de comparação."""
        node = self.parse_comparison_expr()

        while self.current_token() and self.current_token()[0] == 'LOGICAL_OP':
            token = self.current_token()
            self.eat('LOGICAL_OP')
            right = self.parse_comparison_expr()
            node = BinOp(left=node, op=token[1], right=right)

        return node

    def parse_comparison_expr(self):
        """Processa operadores de comparação (`==`, `!=`, `<`, `>`, `<=`, `>=`)."""
        node = self.parse_arithmetic_expr()

        while self.current_token() and self.current_token()[0] == 'COMPARISON_OP':
            token = self.current_token()
            self.eat('COMPARISON_OP')
            right = self.parse_arithmetic_expr()
            node = BinOp(left=node, op=token[1], right=right)

        return node

    def parse_arithmetic_expr(self):
        """Processa expressões aritméticas com operadores + e -."""
        node = self.parse_term()

        while self.current_token() and self.current_token()[0] == 'OP' and self.current_token()[1] in ('+', '-'):
            token = self.current_token()
            self.eat('OP')
            right = self.parse_term()
            node = BinOp(left=node, op=token[1], right=right)

        return node

    def parse_term(self):
        """Processa termos com operadores * e /."""
        node = self.parse_factor()

        while self.current_token() and self.current_token()[0] == 'OP' and self.current_token()[1] in ('*', '/'):
            token = self.current_token()
            self.eat('OP')
            right = self.parse_factor()
            node = BinOp(left=node, op=token[1], right=right)

        return node

    def parse_factor(self):
        """Processa números, variáveis e expressões entre parênteses."""
        token = self.current_token()
        print("[DEBUG] Parsing factor, current token:", token)  # Log para diagnóstico

        if token[0] == 'END' and self.in_for_loop:
            # Ignora `END` apenas dentro do contexto do `for`
            self.eat('END')
            print("[DEBUG] Ignorando `END` no contexto do `for`")  # Log para acompanhar a ignorância do `END`
            return None  # Retorna None para seguir o parsing do `for`
        elif token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Num(token)
        elif token[0] == 'ID':
            self.eat('ID')
            return token[1]
        elif token[0] == 'BOOLEAN':
            self.eat('BOOLEAN')
            return token[1]
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_expression()
            if self.current_token() and self.current_token()[0] == 'RPAREN':
                self.eat('RPAREN')
            else:
                raise Exception("Erro: Parêntese de fechamento ')' esperado.")
            return node
        else:
            raise Exception(f'Erro de sintaxe no fator, token inesperado: {token}')  # Log do erro com token específico

    def assignment_statement(self):
        """Processa uma declaração de atribuição, diferenciando corretamente `=` e `==`."""
        var_name = self.current_token()
        self.eat('ID')

        # Verifica se o token atual é `=` para uma atribuição simples
        if self.current_token() and self.current_token()[0] == 'ASSIGN':
            self.eat('ASSIGN')  # Consome `=`, pois é uma atribuição
            expr = self.parse_expression()  # Processa a expressão completa no lado direito

            # Controle para ignorar o `END` no contexto do `for`
            if self.in_for_loop and self.current_token() and self.current_token()[0] == 'END':
                self.eat('END')  # Ignora o `END` intermediário dentro do `for`
            elif not self.in_for_loop:
                # Exige `END` fora do contexto do `for`
                if self.current_token() and self.current_token()[0] == 'END':
                    self.eat('END')
                else:
                    raise Exception(f"Erro: ';' esperado no final da atribuição, mas encontrado: {self.current_token()}")
            
            return BinOp(left=var_name[1], op='=', right=expr)

        else:
            raise Exception("Erro de sintaxe: Esperado operador `=` após o identificador.")

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
            elif self.current_token()[0] == 'IF':  # Suporte para condicional
                body.append(self.parse_conditional_statement())
            elif self.current_token()[0] == 'WHILE':  # Adiciona o suporte para `RodaARoda`
                body.append(self.parse_while_statement())
            elif self.current_token()[0] == 'FOR':  # Suporte para o laço for
                body.append(self.parse_for_statement())
            elif self.current_token()[0] == 'ID':
                body.append(self.assignment_statement())  # Aqui processamos as atribuições
            elif self.current_token()[0] == 'RETURN':
                body.append(self.return_statement())
            else:
                raise Exception(f"Unexpected token {self.current_token()} in function body")
        
        self.eat('RBRACE')  # Consome '}'
        return FuncDecl(return_type=return_type[1], func_name=func_name[1], body=body)
    
    # Função para processar o corpo de um bloco de código (por exemplo, dentro de condicionais)
    def parse_body(self):
        """Processa o corpo de um bloco, capturando todas as instruções dentro de '{' e '}'."""
        body = []
        while self.current_token() and self.current_token()[0] != 'RBRACE':
            if self.current_token()[0] == 'BREAK':  # Para `CortaPraMim`
                self.eat('BREAK')
                self.eat('END')
                body.append(BreakNode())
            elif self.current_token()[0] == 'INT':
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'FLOAT':
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'BOOLEAN':
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'CHAR':
                body.append(self.variable_declaration())
            elif self.current_token()[0] == 'PRINT':
                body.append(self.print_statement())
            elif self.current_token()[0] == 'INPUT':
                body.append(self.input_statement())
            elif self.current_token()[0] == 'IF':
                body.append(self.parse_conditional_statement())
            elif self.current_token()[0] == 'WHILE': 
                body.append(self.parse_while_statement())
            elif self.current_token()[0] == 'FOR':  # Para `VaiQueEhTua`
                body.append(self.parse_for_statement())
            elif self.current_token()[0] == 'ID':
                body.append(self.assignment_statement())
            elif self.current_token()[0] == 'RETURN':
                body.append(self.return_statement())
            else:
                raise Exception(f"Unexpected token {self.current_token()} in body")
        return body

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