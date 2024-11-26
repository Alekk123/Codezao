import React, { useState, useEffect } from 'react';
import FileExplorer from '../FileExplorer/FileExplorer';
import Editor from '../Editor/Editor';
import Console from '../Console/Console';
import Footer from '../Footer/Footer';
import SaveFileModal from '../SaveFileModal/SaveFileModal';
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
  const [isSavingNewFile, setIsSavingNewFile] = useState(false); // Controle do modal
  const [newFileName, setNewFileName] = useState(''); // Nome do novo arquivo
  const [selectedFolder, setSelectedFolder] = useState(null); // Pasta selecionada
  const [files, setFiles] = useState([]);
  const fetchFiles = () => {
    api.get('/files')
      .then((response) => {
        setFiles(response.data.files);
      })
      .catch((error) => {
        console.error('Erro ao buscar arquivos:', error);
      });
  };
  useEffect(() => {
    

    
  }, []);

  useEffect(() => {
    const checkConnection = () => {
      api.get('/ping')
        .then(() => setConnectionStatus('connected'))
        .catch(() => setConnectionStatus('disconnected'));
    };
  
    checkConnection();
    fetchFiles();
  
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

  const clearConsole = () => {
    setOutput('');
  };

  const saveFile = async () => {
    if (!currentFile) {
      setIsSavingNewFile(true); // Abrir modal para salvar novo arquivo
      return;
    }
  
    try {
      // Verificar conteúdo antes de enviar
      //console.log('Salvando conteúdo:', JSON.stringify(code));
  
      await api.post('/save_or_create', {
        filePath: currentFile.name,
        content: code,
      });
  
      alert('Arquivo salvo com sucesso!');
    } catch (error) {
      alert('Erro ao salvar o arquivo.');
      console.error(error);
    }
  };

  const saveNewFile = async (fileName, folderPath) => {
  try {
    // Enviar o nome do arquivo, pasta e o conteúdo atual do editor
    await api.post('/save_or_create', {
      filePath: folderPath ? `${folderPath}/${fileName}` : fileName,
      content: code, // Inclui o conteúdo do editor
    });

    alert('Arquivo criado e salvo com sucesso!');
    setIsSavingNewFile(false);
    const event = new CustomEvent('refreshFileExplorer');
    window.dispatchEvent(event);
    
    setCurrentFile({ name: folderPath ? `${folderPath}/${fileName}` : fileName }); // Atualiza o arquivo atual
  } catch (error) {
    alert('Erro ao criar ou salvar o arquivo.');
    console.error(error);
  }
};
  
  
  const cancelSaveNewFile = () => {
    setIsSavingNewFile(false);
    setNewFileName('');
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
          <FileExplorer setCode={setCode} setCurrentFile={setCurrentFile} files={files} />
          </LeftPane>

          {/* Editor */}
          <MiddlePane>
          <EditorHeader>
            {/* Título do arquivo */}
            <div className="file-title">
              {currentFile ? currentFile.name : 'Sem título'}
              <button className="close-button" onClick={closeFile} title="Fechar">
                ✕
              </button>
            </div>

            {/* Botões de ação */}
            <div className="action-buttons">
              <button onClick={saveFile} title="Salvar">
                <FaSave size={18} />
              </button>
              <button onClick={compileCode} title="Compilar">
                <FaPlay size={18} />
              </button>
            </div>
          </EditorHeader>
            <Editor code={code} setCode={setCode} isDarkTheme={isDarkTheme} />
          </MiddlePane>

          {/* Console */}
          <RightPane>
            <Console output={output} clearOutput={clearConsole} />
          </RightPane>
        </MainContainer>

        {/* Modal para Salvar Novo Arquivo */}
        <SaveFileModal
          isOpen={isSavingNewFile}
          onSave={saveNewFile}
          onCancel={cancelSaveNewFile}
          folders={files.filter((file) => file.type === 'folder')} // Passa apenas pastas
        />

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
