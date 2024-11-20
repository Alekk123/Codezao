import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tests.test_utils import execute_code_from_file

class TestNestedConditionsAndLoops(unittest.TestCase):

    def test_nested_while_loops(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 i;
            SeViraNos30 j;
            i = 0;

            RodaARoda (i < 3) {
                PoeNaTela("Externo i:");
                PoeNaTela(i);
                j = 0;

                RodaARoda (j < 2) {
                    PoeNaTela("Interno j:");
                    PoeNaTela(j);
                    j = j + 1;
                }
                i = i + 1;
            }

            BeijoDoGordo 0;
        }'''
        result = execute_code_from_file(code, inputs=[])
        expected_output = [
            "Externo i:", "0", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Externo i:", "1", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Externo i:", "2", 
            "Interno j:", "0", 
            "Interno j:", "1"
        ]
        for line in expected_output:
            self.assertIn(line, result)

    def test_nested_for_loops(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 i;
            SeViraNos30 j;

            VaiQueEhTua (i = 0; i < 3; i = i + 1) {
                PoeNaTela("Externo i:");
                PoeNaTela(i);

                VaiQueEhTua (j = 0; j < 2; j = j + 1) {
                    PoeNaTela("Interno j:");
                    PoeNaTela(j);
                }
            }

            BeijoDoGordo 0;
        }'''
        result = execute_code_from_file(code, inputs=[])
        expected_output = [
            "Externo i:", "0", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Externo i:", "1", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Externo i:", "2", 
            "Interno j:", "0", 
            "Interno j:", "1"
        ]
        for line in expected_output:
            self.assertIn(line, result)

    def test_nested_for_while_loops(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 i;
            SeViraNos30 j;

            VaiQueEhTua (i = 0; i < 2; i = i + 1) {
                PoeNaTela("Externo i:");
                PoeNaTela(i);

                j = 0;
                RodaARoda (j < 3) {
                    PoeNaTela("Interno j:");
                    PoeNaTela(j);
                    j = j + 1;
                }
            }

            BeijoDoGordo 0;
        }'''
        result = execute_code_from_file(code, inputs=[])
        expected_output = [
            "Externo i:", "0", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Interno j:", "2",
            "Externo i:", "1", 
            "Interno j:", "0", 
            "Interno j:", "1",
            "Interno j:", "2"
        ]
        for line in expected_output:
            self.assertIn(line, result)

    def test_nested_ifs(self):
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

        inputs = ['15', '6']
        result = execute_code_from_file(code, inputs)
        assert "A > 10 e B >= 5" in result

        inputs = ['5', '0']
        result = execute_code_from_file(code, inputs)
        assert "A <= 10" in result

    def test_nested_if_in_loops(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 i;
            SeViraNos30 j;
            i = 0;

            RodaARoda (i < 3) {
                PoeNaTela("Externo i:");
                PoeNaTela(i);

                EhUmaCiladaBino (i % 2 == 0) {
                    PoeNaTela("i é par");
                } Errrou {
                    PoeNaTela("i é ímpar");
                }

                j = 0;
                RodaARoda (j < 2) {
                    PoeNaTela("Interno j:");
                    PoeNaTela(j);

                    EhUmaCiladaBino (j == 0) {
                        PoeNaTela("j é zero");
                    }
                    j = j + 1;
                }
                i = i + 1;
            }

            BeijoDoGordo 0;
        }'''
        result = execute_code_from_file(code, inputs=[])
        expected_output = [
            "Externo i:", "0", "i é par", 
            "Interno j:", "0", "j é zero", 
            "Interno j:", "1",
            "Externo i:", "1", "i é ímpar", 
            "Interno j:", "0", "j é zero", 
            "Interno j:", "1",
            "Externo i:", "2", "i é par", 
            "Interno j:", "0", "j é zero", 
            "Interno j:", "1"
        ]
        for line in expected_output:
            self.assertIn(line, result)
