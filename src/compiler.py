# Importa todas as classes AST do pyc_parser
from pyc_parser import BinOp, BreakNode, ForNode, IfNode, Num, VarDecl, FuncDecl, Print, Input, FunctionCall, WhileNode

class Compiler:
    def __init__(self):
        self.output = []
        self.variable_types = {}  # Inicializar a tabela de tipos de variáveis

    def compile(self, node, indent_level=0):
        """Função principal que decide como compilar cada tipo de nó."""
        if isinstance(node, FuncDecl):
            return self.compile_function(node, indent_level)
        elif isinstance(node, VarDecl):
            return self.compile_variable(node, indent_level)
        elif isinstance(node, BinOp):
            if node.op == '=':  # Trata a atribuição separadamente
                return self.compile_assignment(node, indent_level)
            else:
                return self.compile_binop(node, indent_level)
        elif isinstance(node, Num):
            return self.compile_num(node, indent_level)
        elif isinstance(node, Print):
            return self.compile_print(node, indent_level)
        elif isinstance(node, Input):
            return self.compile_input(node, indent_level)
        elif isinstance(node, FunctionCall):
            return self.compile_function_call(node, indent_level)
        elif isinstance(node, IfNode):  # Suporte para condicional
            return self.compile_if(node, indent_level)
        elif isinstance(node, WhileNode):  # Suporte para loop While
            return self.compile_while(node, indent_level)
        elif isinstance(node, ForNode):  # Suporte para loop for
            return self.compile_for(node, indent_level)
        elif isinstance(node, BreakNode):
            return self.compile_break(indent_level)
        elif isinstance(node, str):  # Identificadores (variáveis)
            return node  # Retorna o nome da variável diretamente
        elif isinstance(node, int):
            return self.compile_return(node, indent_level)
        elif isinstance(node, list):
            return self.compile_body(node, indent_level)
        return None

    def compile_function(self, node, indent_level=0):
        """Compila uma declaração de função."""
        indent = '    ' * indent_level
        self.output.append(f"{indent}def {node.func_name}():")
        for stmt in node.body:
            compiled_stmt = self.compile(stmt, indent_level + 1)
            if compiled_stmt:
                self.output.append(compiled_stmt)
        self.output.append("")  # Adiciona uma linha em branco após a função

    def compile_variable(self, node, indent_level=0):
        """Compila a declaração de uma variável."""
        indent = '    ' * indent_level
        self.variable_types[node.var_name] = node.var_type
        if node.var_type == 'SeViraNos30':
            value = node.value if node.value else 0
            return f"{indent}{node.var_name} = {value}"
        elif node.var_type == 'QuemQuerDinheiro':
            value = node.value if node.value else 0.0
            return f"{indent}{node.var_name} = {value}"
        elif node.var_type == 'APipaDoVovoNaoSobeMais':
            value = node.value if node.value else "False"
            return f"{indent}{node.var_name} = {value}"
        elif node.var_type == 'Maoee':  # Suporte para char (Maoee)
            value = node.value if node.value else "' '"
            return f"{indent}{node.var_name} = {value}"

    def compile_assignment(self, node, indent_level=0):
        """Compila uma atribuição (assignment)."""
        indent = '    ' * indent_level
        left = node.left
        right = self.compile(node.right, indent_level)
        return f"{indent}{left} = {right}"

    def compile_binop(self, node, indent_level=0):
        """Compila operações binárias."""
        left = self.compile(node.left, indent_level)
        right = self.compile(node.right, indent_level)
        operator = node.op
        operator_map = {
            '&&': 'and', '||': 'or',
            '==': '==', '!=': '!=',
            '<': '<', '>': '>',
            '<=': '<=', '>=': '>=',
            '%': '%'
        }
        operator_python = operator_map.get(operator, operator)
        return f"{left} {operator_python} {right}"

    def compile_num(self, node, indent_level=0):
        """Compila números."""
        # Números são retornados como estão, sem indentação
        return node.value

    def compile_print(self, node, indent_level=0):
        """Compila a instrução de impressão (PoeNaTela)."""
        indent = '    ' * indent_level
        if node.text.startswith('"'):  # Se for string
            return f'{indent}print({node.text})'
        else:  # Se for uma variável
            return f'{indent}print({node.text})'

    def compile_input(self, node, indent_level=0):
        """Compila a instrução de entrada (Receba)."""
        indent = '    ' * indent_level
        var_type = self.variable_types.get(node.var_name, None)
        if var_type == 'SeViraNos30':
            return (f'{indent}try:\n'
                    f'{indent}    {node.var_name} = int(input())\n'
                    f'{indent}except ValueError:\n'
                    f'{indent}    print("Erro: A variável {node.var_name} deve receber um número inteiro!")\n'
                    f'{indent}    raise ValueError("A variável {node.var_name} deve ser um número inteiro!")')
        elif var_type == 'QuemQuerDinheiro':
            return (f'{indent}try:\n'
                    f'{indent}    {node.var_name} = float(input())\n'
                    f'{indent}except ValueError:\n'
                    f'{indent}    print("Erro: A variável {node.var_name} deve receber um número float!")\n'
                    f'{indent}    raise ValueError("A variável {node.var_name} deve ser um número float!")')
        elif var_type == 'APipaDoVovoNaoSobeMais':
            return (f'{indent}while True:\n'
                    f'{indent}    valor = input().lower()\n'
                    f'{indent}    if valor in ["true", "false"]:\n'
                    f'{indent}        {node.var_name} = True if valor == "true" else False\n'
                    f'{indent}        break\n'
                    f'{indent}    else:\n'
                    f'{indent}        print("Erro: A variável {node.var_name} deve receber True ou False!")')
        elif var_type == 'Maoee':  # Validação para char
            return (f'{indent}while True:\n'
                    f'{indent}    valor = input()\n'
                    f'{indent}    if len(valor) == 1:\n'
                    f'{indent}        {node.var_name} = valor\n'
                    f'{indent}        break\n'
                    f'{indent}    else:\n'
                    f'{indent}        print("Erro: A variável {node.var_name} deve receber um único caractere!")')
        else:
            return f'{indent}{node.var_name} = input()'

    def compile_function_call(self, node, indent_level=0):
        """Compila chamadas de função."""
        indent = '    ' * indent_level
        return f'{indent}{node.func_name}()'

    def compile_if(self, node, indent_level=0):
        """Compila instruções condicionais if, elif, else."""
        output = []
        indent = '    ' * indent_level
        for conditional in node.conditionals:
            if conditional[0] == 'if':
                output.append(f"{indent}if {self.compile(conditional[1], indent_level)}:")
                for stmt in conditional[2]:
                    compiled_stmt = self.compile(stmt, indent_level + 1)
                    if compiled_stmt:
                        output.append(compiled_stmt)
            elif conditional[0] == 'elif':
                output.append(f"{indent}elif {self.compile(conditional[1], indent_level)}:")
                for stmt in conditional[2]:
                    compiled_stmt = self.compile(stmt, indent_level + 1)
                    if compiled_stmt:
                        output.append(compiled_stmt)
            elif conditional[0] == 'else':
                output.append(f"{indent}else:")
                for stmt in conditional[1]:
                    compiled_stmt = self.compile(stmt, indent_level + 1)
                    if compiled_stmt:
                        output.append(compiled_stmt)
        return "\n".join(output)

    def compile_while(self, node, indent_level=0):
        """Compila o loop `RodaARoda`."""
        output = []
        indent = '    ' * indent_level
        output.append(f"{indent}while {self.compile(node.condition, indent_level)}:")
        for stmt in node.body:
            compiled_stmt = self.compile(stmt, indent_level + 1)
            if compiled_stmt:
                output.append(compiled_stmt)
        return "\n".join(output)

    def compile_for(self, node, indent_level=0):
        """Compila o laço `VaiQueEhTua`."""
        output = []
        # Inicialização
        init_code = self.compile(node.init, indent_level)
        if init_code:
            output.append(init_code)
        indent = '    ' * indent_level
        # Cabeçalho do loop
        output.append(f"{indent}while {self.compile(node.condition, indent_level)}:")
        # Corpo do loop
        for stmt in node.body:
            compiled_stmt = self.compile(stmt, indent_level + 1)
            if compiled_stmt:
                output.append(compiled_stmt)
        # Incremento
        increment_code = self.compile(node.increment, indent_level + 1)
        if increment_code:
            output.append(increment_code)
        return "\n".join(output)

    def compile_break(self, indent_level=0):
        """Compila a instrução `CortaPraMim` como `break` em Python."""
        indent = '    ' * indent_level
        return f"{indent}break"

    def compile_return(self, node, indent_level=0):
        """Compila instruções de retorno."""
        indent = '    ' * indent_level
        return f"{indent}return {node}"

    def compile_body(self, body, indent_level=0):
        """Compila um bloco de código que é uma lista de instruções."""
        output = []
        for stmt in body:
            compiled_stmt = self.compile(stmt, indent_level)
            if compiled_stmt:
                output.append(compiled_stmt)
        return "\n".join(output)

    def get_output(self):
        """Retorna o código Python gerado."""
        return "\n".join(self.output)