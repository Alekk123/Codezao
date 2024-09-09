import unittest
from tests.test_utils import execute_code_from_file

class TestSignals(unittest.TestCase):

    def test_addition(self):
        """Testa a operação de adição."""
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