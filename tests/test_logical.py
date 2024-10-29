import unittest
from tests.test_utils import execute_code_from_file

class TestLogical(unittest.TestCase):

    def test_logical_and(self):
        code = '''SeViraNos30 OlaTudoBem() {
            APipaDoVovoNaoSobeMais cond1;
            APipaDoVovoNaoSobeMais cond2;
            APipaDoVovoNaoSobeMais resultado;
            Receba(cond1);
            Receba(cond2);
            resultado = cond1 && cond2;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['True', 'True']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_logical_or(self):
        code = '''SeViraNos30 OlaTudoBem() {
            APipaDoVovoNaoSobeMais cond1;
            APipaDoVovoNaoSobeMais cond2;
            APipaDoVovoNaoSobeMais resultado;
            Receba(cond1);
            Receba(cond2);
            resultado = cond1 || cond2;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['False', 'True']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_equal(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a == b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['5', '5']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_not_equal(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a != b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['5', '10']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_greater(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a > b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['10', '5']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_less(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a < b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['5', '10']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_greater_equal(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a >= b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['10', '10']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result

    def test_comparison_less_equal(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            APipaDoVovoNaoSobeMais resultado;
            Receba(a);
            Receba(b);
            resultado = a <= b;
            PoeNaTela("Resultado: ");
            PoeNaTela(resultado);
            BeijoDoGordo 0;
        }'''
        inputs = ['5', '10']
        result = execute_code_from_file(code, inputs)
        assert "Resultado: True" in result