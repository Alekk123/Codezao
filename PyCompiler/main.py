from lexer import tokenize
from pyc_parser import Parser
from compiler import Compiler

code = '''
SeViraNos30 OlaTudoBem() {
    PoeNaTela("Este é o CODEZAO");
    SeViraNos30 resultado = 3 + 5;
    PoeNaTela("A soma de 3 + 5 é:");
    PoeNaTela(resultado);
    Maoee nome;
    PoeNaTela("Digite seu nome:");
    RECEBA(nome);
    PoeNaTela("Seu nome é:");
    PoeNaTela(nome);
    BeijoDoGordo 0;
}
'''

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.parse()

compiler = Compiler()
compiler.compile(ast)
python_code = compiler.get_output()

# Adiciona uma chamada para a função principal 'main' no código gerado
python_code += '\nmain()'

print("Python Code:")
print(python_code)

# Execute o código Python gerado
exec(python_code)
