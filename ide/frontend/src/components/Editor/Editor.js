import React, { useEffect } from 'react';
import MonacoEditor, { monaco } from 'react-monaco-editor';
import { EditorContainer } from './EditorStyles';

function Editor({ code, setCode, isDarkTheme, language = 'codezao', theme = 'vs-dark', options = {} }) {
  useEffect(() => {   
    monaco.languages.register({ id: 'codezao' });
    monaco.languages.setMonarchTokensProvider('codezao', {
      tokenizer: {
        root: [
          [/\b(SeViraNos30|QuemQuerDinheiro|Maoee|APipaDoVovoNaoSobeMais|BeijoDoGordo|PoeNaTela|Receba|EhUmaCiladaBino|VoceEstaCertoDisso|Errrou|RodaARoda|VaiQueEhTua|CortaPraMim)\b/, 'keyword'],
          [/[{}()\[\]]/, '@brackets'],
          [/[;,.]/, 'delimiter'],
          [/"[^"]*"/, 'string'],
          [/\d+/, 'number'],
          [/[a-zA-Z_]\w*/, 'identifier'],
        ],
      },
    });
  }, []);

  useEffect(() => {
    // Registrar o tema personalizado
    monaco.editor.defineTheme('custom-light', {
      base: 'vs', // Base do tema claro
      inherit: true, // Herdar configurações padrão do 'vs'
      rules: [
        { token: 'keyword', foreground: '007ACC', fontStyle: 'bold' }, // Palavras-chave
        { token: 'string', foreground: '6A8759' }, // Strings
        { token: 'number', foreground: 'B5CEA8' }, // Números
        { token: 'identifier', foreground: '333333' }, // Identificadores
      ],
      colors: {
        'editor.background': '#F5F5F5', // Fundo branco suave
        'editor.foreground': '#333333', // Texto principal em cinza escuro
        'editorLineNumber.foreground': '#999999', // Números das linhas em cinza claro
        'editor.selectionBackground': '#DDF4FF', // Fundo de seleção em azul claro
        'editorCursor.foreground': '#007ACC', // Cor do cursor
        'editorWhitespace.foreground': '#CCCCCC', // Espaços em cinza claro
      },
    });
  }, []);

  return (
      <MonacoEditor
        width="100%"
        height="calc(100vh - 40px)"
        language={language}
        theme={isDarkTheme ? theme : 'custom-light'}
        value={code}
        options={{
          selectOnLineNumbers: true,
          ...options, // Permite que `options` seja sobrescrito se passado como prop
        }}
        onChange={(newValue) => setCode(newValue)}
      />
  );
}

export default Editor;
