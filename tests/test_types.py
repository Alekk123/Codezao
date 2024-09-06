import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importa a função de execução de teste do arquivo de utilidades
from test_utils import execute_code_from_file

class TestTypes(unittest.TestCase):
    
    def test_int(self):
        """Testa o tipo SeViraNos30 (int)."""
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 idade;
            PoeNaTela("Digite sua idade: ");
            Receba(idade);
            PoeNaTela("Idade: ");
            PoeNaTela(idade);
            BeijoDoGordo 0;
        }'''
        inputs = ['25']  # Simula a entrada da idade
        result = execute_code_from_file(code, inputs)
        self.assertIn("Idade: 25", result)

    def test_float(self):
        """Testa o tipo QuemQuerDinheiro (float)."""
        code = '''SeViraNos30 OlaTudoBem() {
            QuemQuerDinheiro salario;
            PoeNaTela("Digite seu salário: ");
            Receba(salario);
            PoeNaTela("Salário: ");
            PoeNaTela(salario);
            BeijoDoGordo 0;
        }'''
        inputs = ['2500.50']  # Simula a entrada do salário
        result = execute_code_from_file(code, inputs)
        self.assertIn("Salário: 2500.5", result)

    def test_boolean(self):
        """Testa o tipo APipaDoVovoNaoSobeMais (boolean)."""
        code = '''SeViraNos30 OlaTudoBem() {
            APipaDoVovoNaoSobeMais estaChovendo;
            PoeNaTela("Está chovendo? (True/False): ");
            Receba(estaChovendo);
            PoeNaTela("Está chovendo: ");
            PoeNaTela(estaChovendo);
            BeijoDoGordo 0;
        }'''
        inputs = ['True']  # Simula a entrada booleana
        result = execute_code_from_file(code, inputs)
        self.assertIn("Está chovendo: True", result)

    def test_char(self):
        """Testa o tipo Maoee (char)."""
        code = '''SeViraNos30 OlaTudoBem() {
            Maoee inicial;
            PoeNaTela("Digite uma letra: ");
            Receba(inicial);
            PoeNaTela("Letra digitada: ");
            PoeNaTela(inicial);
            BeijoDoGordo 0;
        }'''
        inputs = ['A']  # Simula a entrada de um caractere
        result = execute_code_from_file(code, inputs)
        self.assertIn("Letra digitada: A", result)
