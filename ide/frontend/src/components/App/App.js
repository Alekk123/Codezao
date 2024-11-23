import React, { useState } from 'react';
import FileExplorer from '../FileExplorer/FileExplorer';
import Editor from '../Editor/Editor';
import Console from '../Console/Console';
import GlobalStyles from '../../styles/GlobalStyles';
import { ThemeProvider } from 'styled-components';
import { darkTheme } from '../../styles/themes';
import api from '../../utils/api';
import { FaPlay, FaSave } from 'react-icons/fa';
import { IoClose } from 'react-icons/io5';
import {
  AppContainer,
  Header,
  MainContainer,
  LeftPane,
  MiddlePane,
  RightPane,
  EditorHeader,
} from './AppStyles';

function App() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [currentFile, setCurrentFile] = useState(null);

  const compileCode = async () => {
    try {
      const response = await api.post('/compile', { code });
      setOutput(response.data.output);
    } catch (error) {
      setOutput('Erro durante a compilação.');
      console.error(error);
    }
  };

  const saveFile = async () => {
    if (!currentFile) {
      alert('Nenhum arquivo aberto para salvar.');
      return;
    }

    try {
      await api.post(`/files/${currentFile.name}`, { content: code });
      alert('Arquivo salvo com sucesso!');
    } catch (error) {
      alert('Erro ao salvar o arquivo.');
      console.error(error);
    }
  };

  const closeFile = () => {
    setCode('');
    setCurrentFile(null);
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <GlobalStyles />
      <AppContainer>
        {/* Header */}
        <Header>
          <span>Codezão IDE</span>
        </Header>

        {/* Corpo Principal */}
        <MainContainer>
          {/* Explorador de Arquivos */}
          <LeftPane>
            <FileExplorer setCode={setCode} setCurrentFile={setCurrentFile} />
          </LeftPane>

          {/* Editor */}
          <MiddlePane>
            <EditorHeader>
              <span>{currentFile ? currentFile.name : 'Sem título'}</span>
              <div>
                <button onClick={compileCode} title="Compilar">
                  <FaPlay size={18} />
                </button>
                <button onClick={saveFile} title="Salvar">
                  <FaSave size={18} />
                </button>
                <button onClick={closeFile} title="Fechar">
                  <IoClose size={18} />
                </button>
              </div>
            </EditorHeader>
            <Editor code={code} setCode={setCode} />
          </MiddlePane>

          {/* Console */}
          <RightPane>
            <Console output={output} />
          </RightPane>
        </MainContainer>
      </AppContainer>
    </ThemeProvider>
  );
}

export default App;
