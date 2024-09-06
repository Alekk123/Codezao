from lexer import tokenize
from pyc_parser import Parser
from compiler import Compiler
from file_upload import upload_file

def main():
    # Abre a janela para selecionar o arquivo .txt
    file_name = upload_file()

    if not file_name:
        print("Nenhum arquivo foi selecionado.")
        return

    # Lê o conteúdo do arquivo
    try:
        with open(file_name, "r") as file:
            code = file.read()
        print("Código lido do arquivo:")
        print(code)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # Tokeniza o código
    try:
        tokens = tokenize(code)
        print("Tokens:", tokens)
    except Exception as e:
        print(f"Erro ao tokenizar o código: {e}")
        return

    # Analisa e cria a AST
    try:
        parser = Parser(tokens)
        ast = parser.parse()
        print("AST:", ast)
    except Exception as e:
        print(f"Erro ao criar a AST: {e}")
        return

    # Compila o código para Python
    try:
        compiler = Compiler()
        compiler.compile(ast)
        python_code = compiler.get_output()
        print("Python Code:")
        print(python_code)
    except Exception as e:
        print(f"Erro ao compilar o código: {e}")
        return

    # Executa o código Python gerado
    try:
         # Cria um escopo local para o exec()
        exec_locals = {}
        exec(python_code, {}, exec_locals) # Executa o código gerado e armazena no exec_locals
        
        # Verifica se a função 'OlaTudoBem' está no escopo local
        if 'OlaTudoBem' in exec_locals:
            print("Função 'OlaTudoBem' encontrada, executando agora...")
            exec_locals['OlaTudoBem']()  # Chama a função gerada
        else:
            # Se a função não for encontrada, exibir uma mensagem detalhada
            print(f"Função principal 'OlaTudoBem' não foi encontrada. Funções disponíveis no escopo: {exec_locals.keys()}")
    except Exception as e:
        print(f"Erro ao executar o código Python: {e}")

if __name__ == "__main__":
    main()
