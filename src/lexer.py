import re

# Definição de tokens usando expressões regulares
TOKEN_SPECIFICATION = [
    ('INT', r'SeViraNos30'),     # Tipo int
    ('FLOAT', r'QuemQuerDinheiro'), # Tipo float
    ('CHAR', r'Maoee'),           # Tipo char
    ('BOOLEAN', r'APipaDoVovoNaoSobeMais'),  # Tipo boolean
    ('RETURN', r'BeijoDoGordo'), # Palavra-chave return
    ('PRINT', r'PoeNaTela'),     # Comando PoeNaTela
    ('INPUT', r'Receba'),        # Comando Receba
    ('NUMBER', r'\d+(\.\d*)?'),  # Números inteiros e de ponto flutuante
    ('ASSIGN', r'='),            # Operador de atribuição
    ('END', r';'),               # Fim de instrução
    ('ID', r'[A-Za-z_áéíóúçÁÉÍÓÚÇ]\w*'),  # Identificadores com suporte a caracteres acentuados
    ('OP', r'[+\-*/]'),          # Operadores aritméticos
    ('STRING', r'\".*?\"'),      # String
    ('LPAREN', r'\('),           # Parênteses de abertura
    ('RPAREN', r'\)'),           # Parênteses de fechamento
    ('LBRACE', r'\{'),           # Chave de abertura
    ('RBRACE', r'\}'),           # Chave de fechamento
    ('NEWLINE', r'\n'),          # Nova linha
    ('SKIP', r'[ \t]+'),         # Espaços e tabulações
    ('MISMATCH', r'.'),          # Qualquer outro caractere
]

# Compilação das expressões regulares
TOKEN_REGEX = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)

def tokenize(code):
    """
    Tokeniza o código de entrada.
    
    Args:
        code (str): Código fonte a ser tokenizado.
    
    Returns:
        list: Lista de tokens identificados no código.
    """
    tokens = []
    
    # Itera sobre todas as correspondências das regex no código
    for match_object in re.finditer(TOKEN_REGEX, code):
        kind = match_object.lastgroup  # Nome do token identificado
        value = match_object.group()   # Valor do token
        
        if kind == 'NEWLINE':
            continue  # Ignora novas linhas
        elif kind == 'SKIP':
            continue  # Ignora espaços e tabulações
        elif kind == 'MISMATCH':
            # Lança erro para caracteres inesperados
            raise RuntimeError(f'Unexpected character {value!r}')
        else:
            tokens.append((kind, value))
    
    return tokens
