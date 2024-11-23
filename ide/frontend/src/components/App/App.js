import React, { useState, useEffect } from 'react';
import FileExplorer from '../FileExplorer/FileExplorer';
import Editor from '../Editor/Editor';
import Console from '../Console/Console';
import Footer from '../Footer/Footer';
import GlobalStyles from '../../styles/GlobalStyles';
import { ThemeProvider } from 'styled-components';
import { darkTheme, lightTheme } from '../../styles/themes';
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
  const [connectionStatus, setConnectionStatus] = useState('disconnected');
  const [isDarkTheme, setIsDarkTheme] = useState(true);

  useEffect(() => {
    const checkConnection = () => {
      api.get('/ping')
        .then(() => setConnectionStatus('connected'))
        .catch(() => setConnectionStatus('disconnected'));
    };
  
    checkConnection();
  
    // Verifica a cada 10 segundos
    const interval = setInterval(checkConnection, 10000);
    return () => clearInterval(interval);
  }, []);

  const compileCode = async () => {
    try {
      const response = await api.post('/compile', { code });
      setOutput(response.data.output);
      setConnectionStatus('connected');
    } catch (error) {
      setOutput('Erro durante a compilação.');
      setConnectionStatus('disconnected');
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
      setConnectionStatus('connected');
    } catch (error) {
      alert('Erro ao salvar o arquivo.');
      setConnectionStatus('disconnected');
      console.error(error);
    }
  };

  const closeFile = () => {
    setCode('');
    setCurrentFile(null);
  };

  const toggleTheme = () => {
    setIsDarkTheme((prev) => !prev);
  };

  useEffect(() => {
    // Verifica a conexão com o backend
    api.get('/ping')
      .then(() => setConnectionStatus('connected'))
      .catch(() => setConnectionStatus('disconnected'));
  }, []);

  return (
    <ThemeProvider theme={isDarkTheme ? darkTheme : lightTheme}>
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
            <Editor code={code} setCode={setCode} isDarkTheme={isDarkTheme} />
          </MiddlePane>

          {/* Console */}
          <RightPane>
            <Console output={output} />
          </RightPane>
        </MainContainer>

        {/* Footer */}
        <Footer
          currentFile={currentFile}
          connectionStatus={connectionStatus}
          lastAction={output}
          toggleTheme={toggleTheme}
          isDarkTheme={isDarkTheme}
        />
        
      </AppContainer>
    </ThemeProvider>
  );
}

export default App;
