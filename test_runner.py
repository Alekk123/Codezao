import unittest
import os
import sys

# Obtém o diretório atual onde o script está sendo executado
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta de testes
test_directory = os.path.join(current_directory, 'tests')

# Adiciona o diretório atual no sys.path para garantir que os imports estão corretos
if current_directory not in sys.path:
    sys.path.insert(0, current_directory)

# Carrega e descobre os testes na pasta 'tests'
loader = unittest.TestLoader()

# Certifique-se de descobrir os testes de uma única vez
suite = loader.discover(start_dir=test_directory, pattern="test_*.py")

# Executa os testes com um log mais detalhado
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)