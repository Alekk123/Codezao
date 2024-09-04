import re

# Definição de tokens usando expressões regulares
TOKEN_SPECIFICATION = [
    ('FUNCTION', r'SeViraNos30(?=\s+OlaTudoBem)'), # Detecta 'SeViraNos30' quando é uma função (main)
    ('MAIN', r'OlaTudoBem'),                # Representa 'main'
    ('RETURN', r'BeijoDoGordo'),            # Representa 'return'
    ('FOR', r'VaiQueEhTua'),                # Representa 'for'
    ('WHILE', r'RodaARoda'),                # Representa 'while'
    ('BREAK', r'CortaPraMim'),              # Representa 'break'
    ('IF', r'EhUmaCiladaBino'),             # Representa 'if'
    ('ELSEIF', r'VoceEstaCertoDisso'),      # Representa 'else if'
    ('ELSE', r'Errrou'),                    # Representa 'else'
    ('INT', r'SeViraNos30'),                # Tipo int
    ('FLOAT', r'QuemQuerDinheiro\?'),       # Tipo float
    ('CHAR', r'Maoee'),                     # Tipo char
    ('BOOLEAN', r'APipaDoVovoNaoSobeMais'), # Tipo boolean
    ('PRINT', r'PoeNaTela'),                # Comando PoeNaTela (printf)
    ('SCANF', r'RECEBA'),                   # Comando RECEBA (scanf)
    ('NUMBER', r'\d+(\.\d*)?'),             # Números inteiros e de ponto flutuante
    ('ASSIGN', r'='),                       # Operador de atribuição
    ('END', r';'),                          # Fim de instrução
    ('ID', r'[A-Za-z_]\w*'),                # Identificadores
    ('OP', r'[+\-*/]'),                     # Operadores aritméticos
    ('STRING', r'\".*?\"'),                 # String
    ('LPAREN', r'\('),                      # Parênteses de abertura
    ('RPAREN', r'\)'),                      # Parênteses de fechamento
    ('LBRACE', r'\{'),                      # Chave de abertura
    ('RBRACE', r'\}'),                      # Chave de fechamento
    ('NEWLINE', r'\n'),                     # Nova linha
    ('SKIP', r'[ \t]+'),                    # Espaços e tabulações
    ('MISMATCH', r'.'),                     # Qualquer outro caractere
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
