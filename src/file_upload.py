import tkinter as tk
from tkinter import filedialog

def upload_file():
    """Abre uma janela para o usuário selecionar o arquivo .txt e retorna o caminho do arquivo."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo .txt",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    return file_path