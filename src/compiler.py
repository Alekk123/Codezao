# Importa todas as classes AST do pyc_parser
from pyc_parser import BinOp, IfNode, Num, VarDecl, FuncDecl, Print, Input, FunctionCall

class Compiler:
    def __init__(self):
        self.output = []
        self.variable_types = {}  # Inicializar a tabela de tipos de variáveis

    def compile(self, node):
        """Função principal que decide como compilar cada tipo de nó."""
        if isinstance(node, FuncDecl):
            return self.compile_function(node)
        elif isinstance(node, VarDecl):
            return self.compile_variable(node)
        elif isinstance(node, BinOp):
            if node.op == '=':  # Trata a atribuição separadamente
                return self.compile_assignment(node)
            else:
                return self.compile_binop(node)
        elif isinstance(node, Num):
            return self.compile_num(node)
        elif isinstance(node, Print):
            return self.compile_print(node)
        elif isinstance(node, Input):
            return self.compile_input(node)
        elif isinstance(node, FunctionCall):
            return self.compile_function_call(node)
        elif isinstance(node, IfNode):  # Suporte para condicional
            return self.compile_if(node)
        elif isinstance(node, str):  # Identificadores (variáveis como 'a', 'b', etc.)
            return node  # Retorna o nome da variável diretamente
        elif isinstance(node, int):
            return self.compile_return(node)
        elif isinstance(node, list):
            return self.compile_body(node)
        return None

# Métodos separados para cada tipo de compilação
    def compile_function(self, node):
        """Compila uma declaração de função."""
        self.output.append(f"def {node.func_name}():")
        for stmt in node.body:
            compiled_stmt = self.compile(stmt)
            if compiled_stmt:
                self.output.append(f"    {compiled_stmt}")
        self.output.append("")  # Adiciona uma linha em branco após a função

    def compile_variable(self, node):
        """Compila a declaração de uma variável."""
        self.variable_types[node.var_name] = node.var_type
        if node.var_type == 'SeViraNos30':
            value = node.value if node.value else 0
            return f"{node.var_name} = {value}"
        elif node.var_type == 'QuemQuerDinheiro':
            value = node.value if node.value else 0.0
            return f"{node.var_name} = {value}"
        elif node.var_type == 'APipaDoVovoNaoSobeMais':
            value = node.value if node.value else "False"
            return f"{node.var_name} = {value}"
        elif node.var_type == 'Maoee':  # Suporte para char (Maoee)
            value = node.value if node.value else "' '"
            return f"{node.var_name} = {value}"
        
    def compile_if(self, node, indent_level=0):
        """Compila instruções condicionais if, elif, else com controle de indentação adequado para nested conditions."""
        output = []
        base_indent = '    ' * indent_level  # Nível de indentação para o 'if'
        elif_else_indent = '    ' * (indent_level + 1)  # Nível de indentação para o 'elif' e 'else'
        inner_indent = '    ' * (indent_level + 2)  # Nível de indentação para o conteúdo interno dos blocos

        nested_level = 0  # Controle do nível de indentação para if aninhados

        for conditional in node.conditionals:
            if conditional[0] == 'if':
                current_indent = base_indent if nested_level == 0 else '    ' * (indent_level + nested_level)
                output.append(f"{current_indent}if {self.compile(conditional[1])}:")
                
                for stmt in conditional[2]:  # Bloco interno do 'if'
                    compiled_stmt = self.compile(stmt)
                    if compiled_stmt:
                        output.append(f"{current_indent}{'    ' * 2}{compiled_stmt}")

                nested_level += 1  # Aumenta o nível de indentação para if aninhado

            elif conditional[0] == 'elif':
                output.append(f"{elif_else_indent}elif {self.compile(conditional[1])}:")
                
                for stmt in conditional[2]:  # Bloco interno do 'elif'
                    compiled_stmt = self.compile(stmt)
                    if compiled_stmt:
                        output.append(f"{inner_indent}{compiled_stmt}")

            elif conditional[0] == 'else':
                current_else_indent = base_indent if nested_level == 0 else elif_else_indent
                output.append(f"{current_else_indent}else:")
                
                for stmt in conditional[1]:  # Bloco interno do 'else'
                    compiled_stmt = self.compile(stmt)
                    if compiled_stmt:
                        output.append(f"{inner_indent}{compiled_stmt}")
                
                if nested_level > 0:
                    nested_level -= 1  # Diminui o nível ao sair do bloco aninhado

        compiled_code = "\n".join(output)
        
        # Log para verificar a formatação e a lógica
        print("Código condicional compilado:\n", compiled_code)
        
        return compiled_code

    def compile_binop(self, node):
        """Compila operações binárias com verificações de segurança e depuração detalhada."""
        # Verifica se os operadores e operandos existem
        if node.left is None or node.right is None or node.op is None:
            raise Exception(f"Erro: Operadores ou operandos inválidos. Node.left: {node.left}, Node.op: {node.op}, Node.right: {node.right}")

        # Exibe informações de depuração sobre o nó de operação binária
        #print(f"Compilando BinOp: {node.left} {node.op} {node.right}")
    
        # Compila os operandos esquerdo e direito
        left = self.compile(node.left)
        right = self.compile(node.right)
    
        # Verifica se os operandos são válidos
        if left is None:
            raise Exception(f"Erro: Operando esquerdo é None. Node.left: {node.left}")
        if right is None:
            raise Exception(f"Erro: Operando direito é None. Node.right: {node.right}")
    
        # Verifica se o operador é válido
        operator = node.op 
        if operator not in ['+', '-', '*', '/', '&&', '||', '==', '!=', '<', '>', '<=', '>=']:
            raise Exception(f"Operador binário inválido: {operator}")
        
        # Mapeamento de operadores para Python
        operator_map = {
            '&&': 'and', '||': 'or', 
            '==': '==', '!=': '!=', 
            '<': '<', '>': '>', 
            '<=': '<=', '>=': '>='
        }
        
        operator_python = operator_map.get(node.op, node.op)
    
        # Exibe os operandos compilados para depuração
        #print(f"Operando esquerdo compilado: {left}")
        #print(f"Operando direito compilado: {right}")
    
        # Retorna a operação binária compilada no formato de Python
        return f"{left} {operator_python} {right}"
    
    def compile_assignment(self, node):
        """Compila uma atribuição (assignment)."""
        left = node.left
        right = self.compile(node.right)  # Expressão que está sendo atribuída
        return f"{left} = {right}"

    def compile_num(self, node):
        """Compila números."""
        return node.value

    def compile_print(self, node):
        """Compila a instrução de impressão (PoeNaTela)."""
        if node.text.startswith('"'):  # Se for string
            return f'print({node.text})'
        else:  # Se for uma variável
            return f'print({node.text})'

    def compile_input(self, node):
        """Compila a instrução de entrada (Receba)."""
        var_type = self.variable_types.get(node.var_name, None)
        if var_type == 'SeViraNos30':
            return (f'try:\n'
                    f'      {node.var_name} = int(input())\n'
                    f'    except ValueError:\n'
                    f'      print("Erro: A variável {node.var_name} deve receber um número inteiro!")\n'
                    f'      raise ValueError("A variável {node.var_name} deve ser um número inteiro!")')
        elif var_type == 'QuemQuerDinheiro':
            return (f'try:\n'
                    f'      {node.var_name} = float(input())\n'
                    f'    except ValueError:\n'
                    f'      print("Erro: A variável {node.var_name} deve receber um número float!")\n'
                    f'      raise ValueError("A variável {node.var_name} deve ser um número float!")')
        elif var_type == 'APipaDoVovoNaoSobeMais':
            return (f'while True:\n'
                    f'      valor = input().lower()\n'
                    f'      if valor in ["true", "false"]:\n'
                    f'          {node.var_name} = True if valor == "true" else False\n'
                    f'          break\n'
                    f'      else:\n'
                    f'          print("Erro: A variável {node.var_name} deve receber True ou False!")')
        elif var_type == 'Maoee':  # Validação para char
            return (f'while True:\n'
                    f'      valor = input()\n'
                    f'      if len(valor) == 1:\n'
                    f'          {node.var_name} = valor\n'
                    f'          break\n'
                    f'      else:\n'
                    f'          print("Erro: A variável {node.var_name} deve receber um único caractere!")')
        else:
            return f'{node.var_name} = input()'

    def compile_function_call(self, node):
        """Compila chamadas de função."""
        return f'{node.func_name}()'

    def compile_return(self, node):
        """Compila instruções de retorno."""
        return f"return {node}"

    def compile_body(self, body):
        """Compila um bloco de código que é uma lista de instruções."""
        for stmt in body:
            self.compile(stmt)

    def get_output(self):
        """Retorna o código Python gerado."""
        return "\n".join(self.output)