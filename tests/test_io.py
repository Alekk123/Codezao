import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importa a função de execução de teste do arquivo de utilidades
from test_utils import execute_code_from_file

class TestIO(unittest.TestCase):
    
    def test_input_output(self):
        """Testa entrada (Receba) e saída (PoeNaTela)."""
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 idade;
            PoeNaTela("Digite sua idade: ");
            Receba(idade);
            PoeNaTela("Idade: ");
            PoeNaTela(idade);
            BeijoDoGordo 0;
        }'''
        inputs = ['30']  # Simula a entrada da idade
        result = execute_code_from_file(code, inputs)
        self.assertIn("Idade: 30", result)
