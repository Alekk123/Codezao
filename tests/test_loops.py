import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tests.test_utils import execute_code_from_file

class TestWhileLoop(unittest.TestCase):

    def test_basic_while_loop(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 contador;
            contador = 0;

            RodaARoda (contador < 3) {
                PoeNaTela("Contador em: ");
                PoeNaTela(contador);
                contador = contador + 1;
            }

            BeijoDoGordo 0;
        }'''
        # Executa o código e verifica se o loop foi executado corretamente
        result = execute_code_from_file(code, inputs=[])
        
        # Verifica o output esperado para o loop
        assert "Contador em: 0" in result
        assert "Contador em: 1" in result
        assert "Contador em: 2" in result
        assert "Contador em: 3" not in result  # Verifica que o loop parou em 3

    def test_while_loop_with_input(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 limite;
            SeViraNos30 contador;
            contador = 0;

            PoeNaTela("Digite o limite para o contador:");
            Receba(limite);

            RodaARoda (contador < limite) {
                PoeNaTela("Contador em: ");
                PoeNaTela(contador);
                contador = contador + 1;
            }

            BeijoDoGordo 0;
        }'''
        # Fornece um valor de entrada para limitar o loop
        inputs = ['2']
        result = execute_code_from_file(code, inputs)
        
        # Verifica o output esperado para o limite de 2
        assert "Contador em: 0" in result
        assert "Contador em: 1" in result
        assert "Contador em: 2" not in result  # O loop deve parar antes de 2
    
    def test_for_loop(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 contador;
            contador = 0;

            VaiQueEhTua (contador = 0 ; contador < 5 ; contador = contador + 1) {
                PoeNaTela("Contador em: ");
                PoeNaTela(contador);
            }

            BeijoDoGordo 0;
        }'''
        result = execute_code_from_file(code, inputs=[])
        expected_output = [
            "Contador em:", 
            "0", 
            "Contador em:", 
            "1", 
            "Contador em:", 
            "2", 
            "Contador em:", 
            "3", 
            "Contador em:", 
            "4"
        ]
        for line in expected_output:
            self.assertIn(line, result)