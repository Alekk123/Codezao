import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tests.test_utils import execute_code_from_file

class TestConditionals(unittest.TestCase):

    def test_if_only(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            Receba(a);
            EhUmaCiladaBino (a > 10) {
                PoeNaTela("Maior que 10");
            }
            BeijoDoGordo 0;
        }'''
        inputs = ['15']
        result = execute_code_from_file(code, inputs)
        assert "Maior que 10" in result

    def test_if_else(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            Receba(a);
            EhUmaCiladaBino (a > 10) {
                PoeNaTela("Maior que 10");
            } Errrou {
                PoeNaTela("10 ou menor");
            }
            BeijoDoGordo 0;
        }'''
        inputs = ['5']
        result = execute_code_from_file(code, inputs)
        assert "10 ou menor" in result

    def test_if_elseif_else(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            Receba(a);
            EhUmaCiladaBino (a > 10) {
                PoeNaTela("Maior que 10");
            } VoceEstaCertoDisso (a == 10) {
                PoeNaTela("Igual a 10");
            } Errrou {
                PoeNaTela("Menor que 10");
            }
            BeijoDoGordo 0;
        }'''
        inputs = ['10']
        result = execute_code_from_file(code, inputs)
        assert "Igual a 10" in result
        
    
    def test_nested_conditionals(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 a;
            SeViraNos30 b;
            Receba(a);
            Receba(b);
            EhUmaCiladaBino (a > 10) {
                EhUmaCiladaBino (b < 5) {
                    PoeNaTela("A > 10 e B < 5");
                } Errrou {
                    PoeNaTela("A > 10 e B >= 5");
                }
            } Errrou {
                PoeNaTela("A <= 10");
            }
            BeijoDoGordo 0;
        }'''
        inputs = ['15', '3']
        result = execute_code_from_file(code, inputs)
        assert "A > 10 e B < 5" in result
    