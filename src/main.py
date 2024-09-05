from ast import main
from lexer import tokenize
from pyc_parser import Parser
from compiler import Compiler

code = '''
int main() {
    PoeNaTela("Hello, World!");
    return 0;
}
'''

tokens = tokenize(code)
print("Tokens:", tokens)

parser = Parser(tokens)
ast = parser.parse()
print("AST:", ast)

compiler = Compiler()
compiler.compile(ast)
python_code = compiler.get_output()

print("Python Code:")
print(python_code)

# Execute o código Python gerado
exec(python_code)

# Chama a função main gerada
main()
