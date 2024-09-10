import unittest
from tests.test_utils import execute_code_from_file

class TestOperations(unittest.TestCase):

    def test_addition(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            PoeNaTela("Digite dois números: ");
            Receba(a);
            Receba(b);
            resultado = a + b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['10', '20']  # a = 10, b = 20
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 30" in result
        
    def test_subtraction(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            PoeNaTela("Digite dois números: ");
            Receba(a);
            Receba(b);
            resultado = a - b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['20', '10']  # a = 20, b = 10
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 10" in result

    def test_multiplication(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            PoeNaTela("Digite dois números: ");
            Receba(a);
            Receba(b);
            resultado = a * b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['3', '5']  # a = 3, b = 5
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 15" in result

    def test_division(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            PoeNaTela("Digite dois números: ");
            Receba(a);
            Receba(b);
            resultado = a / b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['20', '5']  # a = 20, b = 5
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 4" in result