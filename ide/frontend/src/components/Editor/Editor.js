import React, { useEffect } from 'react';
import MonacoEditor, { monaco } from 'react-monaco-editor';
import { EditorContainer } from './EditorStyles';

function Editor({ code, setCode }) {
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

  const options = {
    selectOnLineNumbers: true,
  };

  return (
    <EditorContainer>
      <MonacoEditor
        language="codezao"
        theme="vs-dark"
        value={code}
        options={options}
        onChange={(newValue) => setCode(newValue)}
      />
    </EditorContainer>
  );
}

export default Editor;
