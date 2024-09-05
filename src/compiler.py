# Importa todas as classes AST do pyc_parser
from pyc_parser import BinOp, Num, VarDecl, FuncDecl, Print

class Compiler:
    def __init__(self):
        self.output = []

    def compile(self, node):
        if isinstance(node, FuncDecl):
            self.output.append(f"def {node.func_name}():")
            for stmt in node.body:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(f"    {compiled_stmt}")
            self.output.append("")  # Adiciona uma linha em branco após a função
        elif isinstance(node, VarDecl):
            return f"{node.var_name} = {node.value.value}"
        elif isinstance(node, BinOp):
            left = self.compile(node.left)
            right = self.compile(node.right)
            return f"{left} {node.op} {right}"
        elif isinstance(node, Num):
            return node.value
        elif isinstance(node, Print):
            return f'print({node.text})'
        elif isinstance(node, int):  # Ajuste para reconhecer nós de retorno que são inteiros
            return f"return {node}"  # Retorna corretamente em Python
        elif isinstance(node, list):  # Quando compilar o corpo da função que pode ser uma lista
            for stmt in node:
                self.compile(stmt)
        return None

    def get_output(self):
        return "\n".join(self.output)

# Exemplo de uso:
if __name__ == "__main__":
    from lexer import tokenize
    from pyc_parser import Parser

    code = '''
    int main() {
        PoeNaTela("Hello, World!");
        return 0;
    }
    '''

    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    
    compiler = Compiler()
    compiler.compile(ast)
    python_code = compiler.get_output()

    print("Python Code:")
    print(python_code)

    # Execute o código Python gerado
    exec(python_code)


