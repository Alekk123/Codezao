from lexer import tokenize
from pyc_parser import Parser
from compiler import Compiler
from file_upload import upload_file

def read_file(file_name):
    """
    Lê o conteúdo de um arquivo e retorna o código fonte.
    
    Args:
        file_name (str): Caminho do arquivo.
        
    Returns:
        str: Código lido do arquivo.
    """
    try:
        with open(file_name, "r") as file:
            code = file.read()
        print("Código lido do arquivo:")
        #print(code)
        return code
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def process_tokens(code):
    """
    Tokeniza o código fonte.
    
    Args:
        code (str): Código fonte a ser tokenizado.
        
    Returns:
        list: Lista de tokens.
    """
    try:
        tokens = tokenize(code)
        #print("Tokens:", tokens)
        return tokens
    except Exception as e:
        print(f"Erro ao tokenizar o código: {e}")
        return None

def parse_code(tokens):
    """
    Cria a AST a partir dos tokens.
    
    Args:
        tokens (list): Lista de tokens.
        
    Returns:
        AST: Árvore de Sintaxe Abstrata gerada a partir dos tokens.
    """
    try:
        parser = Parser(tokens)
        ast = parser.parse()
        print("AST:", ast)
        return ast
    except Exception as e:
        print(f"Erro ao criar a AST: {e}")
        return None

def compile_code(ast):
    """
    Compila a AST para código Python.
    
    Args:
        ast (AST): Árvore de Sintaxe Abstrata a ser compilada.
        
    Returns:
        str: Código Python gerado a partir da AST.
    """
    try:
        compiler = Compiler()
        compiler.compile(ast)
        python_code = compiler.get_output()
        print("Python Code:")
        print(python_code)
        return python_code
    except Exception as e:
        print(f"Erro ao compilar o código: {e}")
        return None

def execute_code(python_code):
    """
    Executa o código Python gerado e chama a função principal 'OlaTudoBem'.
    
    Args:
        python_code (str): Código Python gerado.
    """
    try:
        # Cria um escopo local para o exec()
        exec_locals = {}
        exec(python_code, {}, exec_locals)  # Executa o código gerado e armazena no exec_locals
        
        # Verifica se a função 'OlaTudoBem' está no escopo local
        if 'OlaTudoBem' in exec_locals:
            print("Função 'OlaTudoBem' encontrada, executando agora...")
            exec_locals['OlaTudoBem']()  # Chama a função gerada
        else:
            # Se a função não for encontrada, exibir uma mensagem detalhada
            print(f"Função principal 'OlaTudoBem' não foi encontrada. Funções disponíveis no escopo: {exec_locals.keys()}")
    except Exception as e:
        print(f"Erro ao executar o código Python: {e}")

def main():
    """
    Função principal que organiza o fluxo: leitura do arquivo, tokenização, análise, compilação e execução.
    """
    # Abre a janela para selecionar o arquivo .txt
    file_name = upload_file()

    if not file_name:
        print("Nenhum arquivo foi selecionado.")
        return

    # Lê o conteúdo do arquivo
    code = read_file(file_name)
    if not code:
        return

    # Tokeniza o código
    tokens = process_tokens(code)
    if not tokens:
        return

    # Analisa e cria a AST
    ast = parse_code(tokens)
    if not ast:
        return

    # Compila o código para Python
    python_code = compile_code(ast)
    if not python_code:
        return

    # Executa o código Python gerado
    execute_code(python_code)

if __name__ == "__main__":
    main()
