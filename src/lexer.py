import re

# Definição de tokens usando expressões regulares
TOKEN_SPECIFICATION = [
    ('INT', r'SeViraNos30'),     # Tipo int
    ('FLOAT', r'float'),         # Tipo float
    ('CHAR', r'char'),           # Tipo char
#    ('MAIN', r'OlaTudoBem'),    # Função principal
    ('RETURN', r'BeijoDoGordo'), # Palavra-chave return
    ('PRINT', r'PoeNaTela'),     # Comando PoeNaTela
    ('INPUT', r'Receba'),        # Comando Receba (novo)
    ('NUMBER', r'\d+(\.\d*)?'),  # Números inteiros e de ponto flutuante
    ('ASSIGN', r'='),            # Operador de atribuição
    ('END', r';'),               # Fim de instrução
    ('ID', r'[A-Za-z_]\w*'),     # Identificadores
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
TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)

def tokenize(code):
    tokens = []
    for mo in re.finditer(TOKEN_REGEX, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE':
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        else:
            tokens.append((kind, value))
    return tokens
