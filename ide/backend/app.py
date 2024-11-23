from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Ajuste o caminho para importar o compilador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from main import process_tokens, parse_code, compile_code

app = Flask(__name__)
CORS(app)

FILES_DIR = os.path.abspath('../../Code.Codezao')

def list_files_and_folders(base_dir):
    """
    Lista recursivamente arquivos e pastas em uma estrutura hierárquica.
    """
    items = []
    try:
        for entry in os.scandir(base_dir):
            if entry.is_dir():
                items.append({
                    'type': 'folder',
                    'name': entry.name,
                    'files': list_files_and_folders(entry.path)  # Lista arquivos dentro da pasta
                })
            elif entry.is_file():
                items.append({
                    'type': 'file',
                    'name': entry.name
                })
    except Exception as e:
        print(f"Erro ao listar {base_dir}: {e}")
    return items

@app.route('/files', methods=['GET'])
def get_files():
    """
    Endpoint que retorna a lista de arquivos e pastas na estrutura hierárquica.
    """
    try:
        files_structure = list_files_and_folders(FILES_DIR)
        return jsonify({'files': files_structure}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/files/<path:filename>', methods=['GET'])
def get_file_content(filename):
    """
    Retorna o conteúdo de um arquivo específico.
    """
    filepath = os.path.join(FILES_DIR, filename)
    if os.path.exists(filepath) and os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return jsonify({'content': content}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Arquivo não encontrado'}), 404

@app.route('/compile', methods=['POST'])
def compile():
    """Compila e executa código enviado pelo frontend."""
    data = request.get_json()
    code = data.get('code', '')
    try:
        output = compile_and_run(code)
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'output': str(e)}), 500
    
@app.route('/rename', methods=['POST'])
def rename_item():
    """Renomeia um arquivo ou pasta."""
    data = request.get_json()
    old_name = data.get('oldName')
    new_name = data.get('newName')

    if not old_name or not new_name:
        return jsonify({'error': 'Nome antigo e novo são necessários'}), 400

    old_path = os.path.join(FILES_DIR, old_name)
    new_path = os.path.join(FILES_DIR, new_name)

    if not os.path.exists(old_path):
        return jsonify({'error': 'Arquivo ou pasta não encontrado'}), 404

    if os.path.exists(new_path):
        return jsonify({'error': 'Um item com o novo nome já existe'}), 400

    try:
        os.rename(old_path, new_path)
        return jsonify({'message': 'Renomeado com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def compile_and_run(code):
    """Compila e executa o código, capturando a saída."""
    tokens = process_tokens(code)
    ast = parse_code(tokens)
    python_code = compile_code(ast)

    import io
    import contextlib
    exec_locals = {}
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        exec(python_code, {}, exec_locals)
        if 'OlaTudoBem' in exec_locals:
            exec_locals['OlaTudoBem']()
    output = f.getvalue()
    return output

if __name__ == '__main__':
    app.run(debug=True)
