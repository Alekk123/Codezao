# Importa todas as classes AST do pyc_parser
from pyc_parser import BinOp, Num, VarDecl, FuncDecl, Print, Input, FunctionCall

class Compiler:
    def __init__(self):
        self.output = []
        self.variable_types = {}  # Inicializar a tabela de tipos de variáveis

    def compile(self, node):
        if isinstance(node, FuncDecl):
            self.output.append(f"def {node.func_name}():")
            for stmt in node.body:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(f"    {compiled_stmt}")
            self.output.append("")  # Adiciona uma linha em branco após a função
        elif isinstance(node, VarDecl):
            # Armazena o tipo da variável na tabela de tipos
            self.variable_types[node.var_name] = node.var_type
            if node.var_type == 'SeViraNos30':
                value = node.value if node.value else 0
                return f"{node.var_name} = {value}"
        elif isinstance(node, BinOp):
            left = self.compile(node.left)
            right = self.compile(node.right)
            return f"{left} {node.op} {right}"
        elif isinstance(node, Num):
            return node.value
        elif isinstance(node, Print):
             # Verifica se é uma string ou uma variável para imprimir
            if node.text.startswith('"'):  # Verifica se é uma string
                return f'print({node.text})'
            else:  # Se for um identificador (variável)
                return f'print({node.text})'
        elif isinstance(node, Input):  # Suporte para Receba
            # Verifica o tipo da variável antes de gerar o código de input
            var_type = self.variable_types.get(node.var_name, None)
            if var_type == 'SeViraNos30':
                # Se a variável for do tipo SeViraNos30, garante que o valor inserido seja um número inteiro
                return (f'try:\n'
                        f'      {node.var_name} = int(input())\n'
                        f'    except ValueError:\n'
                        f'      print("Erro: A variável {node.var_name} deve receber um número inteiro!")\n'
                        f'      raise ValueError("A variável {node.var_name} deve ser um número inteiro!")')
            else:
                # Se for outro tipo, aceita qualquer valor
                return f'{node.var_name} = input()'
        elif isinstance(node, FunctionCall):  # Suporte para chamadas de função
            return f'{node.func_name}()'
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


