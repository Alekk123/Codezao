from pyc_parser import BinOp, Num, VarDecl, FuncDecl, Output, Input, If, While, For, Break

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
            if node.value:
                return f"{node.var_name} = {self.compile(node.value)}"
            else:
                return f"{node.var_name} = None"

        elif isinstance(node, BinOp):
            left = self.compile(node.left)
            right = self.compile(node.right)
            return f"{left} {node.op} {right}"

        elif isinstance(node, Num):
            return str(node.value)  # Retorna o valor numérico como string

        elif isinstance(node, Output):
            if isinstance(node.text, tuple) and node.text[0] == 'ID':
                return f'print({node.text[1]})'  # Corrige o uso de ID para variáveis
            else:
                return f'print({node.text})'

        elif isinstance(node, Input):
            return f'{node.var_name} = input()'

        elif isinstance(node, If):
            code = f"if {self.compile(node.condition)}:"
            self.output.append(code)
            for stmt in node.then_body:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(f"    {compiled_stmt}")
            if node.else_body:
                self.output.append("else:")
                for stmt in node.else_body:
                    compiled_stmt = self.compile(stmt)
                    if compiled_stmt:
                        self.output.append(f"    {compiled_stmt}")
            return None

        elif isinstance(node, While):
            self.output.append(f"while {self.compile(node.condition)}:")
            for stmt in node.body:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(f"    {compiled_stmt}")
            return None

        elif isinstance(node, For):
            init = self.compile(node.init)
            condition = self.compile(node.condition)
            increment = self.compile(node.increment)
            self.output.append(f"{init}")
            self.output.append(f"while {condition}:")
            for stmt in node.body:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(f"    {compiled_stmt}")
            self.output.append(f"    {increment}")
            return None

        elif isinstance(node, Break):
            return "break"

        elif isinstance(node, str):
            return node

        elif isinstance(node, list):
            for stmt in node:
                compiled_stmt = self.compile(stmt)
                if compiled_stmt:
                    self.output.append(compiled_stmt)

        elif isinstance(node, tuple):  # Adicionado para tratar retornos numéricos
            if node[0] == 'NUMBER':
                return f"return {node[1]}"
            elif node[0] == 'ID':
                return node[1]  # Retorna o nome da variável

        return None

    def get_output(self):
        return "\n".join(self.output)

# Exemplo de uso:
if __name__ == "__main__":
    from lexer import tokenize
    from pyc_parser import Parser

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

    print("Python Code:")
    print(python_code)

    # Execute o código Python gerado
    exec(python_code)
