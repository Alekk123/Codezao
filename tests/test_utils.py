from lexer import tokenize
from pyc_parser import Parser
from compiler import Compiler

def execute_code_from_file(code, inputs):
    """Simula a execução do código da linguagem customizada com entradas automáticas e captura as saídas de print."""
    result = []
    input_iterator = iter(inputs)  # Cria um iterador para as entradas simuladas
    
    def capture_print(*args, sep=' ', end=''):
        """Captura as saídas do print e as armazena no resultado sem adicionar quebras de linha desnecessárias."""
        formatted_output = sep.join(str(arg) for arg in args) + end
        result.append(formatted_output)

    def mock_input(prompt=''):
        """Mock da função input que aceita o argumento (prompt) e retorna o próximo valor da lista de entradas simuladas."""
        return next(input_iterator)

    # Tokeniza o código
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    
    compiler = Compiler()
    compiler.compile(ast)
    python_code = compiler.get_output()

    # Substitui a função print para capturar a saída e a função input para simular entradas
    exec_locals = {}
    exec(python_code, {'print': capture_print, 'input': mock_input}, exec_locals)
    
    # Verifica se a função 'OlaTudoBem' está no escopo local
    if 'OlaTudoBem' in exec_locals:
        exec_locals['OlaTudoBem']()  # Chama a função gerada
    
    # Junta todas as saídas sem adicionar espaços ou quebras de linha desnecessárias
    return "".join(result)
