import unittest
import sys
import os

# Adiciona o caminho da pasta 'src' para importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tests.test_utils import execute_code_from_file

class TestLoopBreak(unittest.TestCase):

    def test_while_with_break(self):
        code = '''SeViraNos30 OlaTudoBem() {
            SeViraNos30 contador;
            contador = 0;

            RodaARoda (contador < 10) {
                PoeNaTela("Contador em: ");
                PoeNaTela(contador);
                contador = contador + 1;

                EhUmaCiladaBino (contador == 5) {
                    PoeNaTela("Interrompendo o loop.");
                    CortaPraMim;
                }
            }

            BeijoDoGordo 0;
        }'''
        
        inputs = []
        result = execute_code_from_file(code, inputs)
        
        # Verificações das saídas esperadas
        self.assertIn("Contador em:", result)
        self.assertIn("0", result)
        self.assertIn("Interrompendo o loop.", result)
        self.assertNotIn("Contador em: 5", result)  # Confirma que o loop encerrou antes de contar 5