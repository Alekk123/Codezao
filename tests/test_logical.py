import unittest
from tests.test_utils import execute_code_from_file

class TestLogical(unittest.TestCase):

    def test_logical_and(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            Receba(a);
            Receba(b);
            resultado = a && b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['1', '1']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 1" in result

    def test_logical_equality(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            SeViraNos30 resultado;
            Receba(a);
            Receba(b);
            resultado = a == b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['10', '10']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: 1" in result  # Assumindo que 1 representa True no compilador