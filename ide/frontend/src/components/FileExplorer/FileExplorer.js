import React, { useState, useEffect } from 'react';
import api from '../../utils/api';
import {
  FiFolder,
  FiChevronDown,
  FiChevronRight,
  FiFile,
  FiEdit,
  FiTrash,
  FiPlus,
  FiSearch,
} from 'react-icons/fi';
import { ExplorerContainer } from './FileExplorerStyles';

function FileExplorer({ setCode, setCurrentFile }) {
  const [files, setFiles] = useState([]);
  const [expandedFolders, setExpandedFolders] = useState({});
  const [newItem, setNewItem] = useState(null);
  const [loading, setLoading] = useState(true);
  const [renaming, setRenaming] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState(null);
  const [currentFolder, setCurrentFolder] = useState(null);

  useEffect(() => {

    fetchFiles();
    
    const handleRefresh = () => {
      fetchFiles();
    };
    // Escuta o evento customizado
    window.addEventListener('refreshFileExplorer', handleRefresh);

    // Cleanup no unmount
    return () => {
      window.removeEventListener('refreshFileExplorer', handleRefresh);
    };


    
  }, []);

  const fetchFiles = () => {
    setLoading(true);
    api.get('/files')
      .then((response) => {
        setFiles(response.data.files);
      })
      .catch((error) => {
        console.error('Erro ao buscar arquivos:', error);
      })
      .finally(() => setLoading(false));
  };

  const toggleFolder = (folderName) => {
    setExpandedFolders((prev) => ({
      ...prev,
      [folderName]: !prev[folderName],
    }));
  };

  const handleCreate = (isFolder) => {
    setNewItem({ isFolder, name: '', parent: currentFolder });
  };

  const saveNewItem = () => {
    if (!newItem.name.trim()) {
      alert('O nome não pode ser vazio.');
      return;
    }
  
    api.post('/create', {
      name: newItem.name,
      isFolder: newItem.isFolder,
      parent: newItem.parent, // Envia o caminho da pasta pai
    })
      .then(() => {
        fetchFiles();
        setNewItem(null);
      })
      .catch((error) => {
        console.error('Erro ao criar item:', error);
      });
  };

  const cancelNewItem = () => {
    setNewItem(null);
  };

  const selectFolder = (folder) => {
    setCurrentFolder(folder);
  };

  const handleRename = (fileOrFolder, newName, currentPath = '') => {
    if (!newName.trim()) {
      cancelRenaming();
      return;
    }
  
    // Caminho completo antigo e novo
    const oldFullPath = currentPath ? `${currentPath}/${fileOrFolder.name}` : fileOrFolder.name;
    const newFullPath = currentPath ? `${currentPath}/${newName}` : newName;
  
    api.post('/rename', { oldName: oldFullPath, newName: newFullPath })
      .then(() => {
        fetchFiles(); // Atualiza a lista de arquivos após renomear
        setRenaming(null);
      })
      .catch((error) => {
        console.error('Erro ao renomear item:', error);
      });
  };

  const cancelRenaming = () => {
    setRenaming(null);
  };

  const handleDelete = (fileOrFolder, currentPath = '') => {
    const confirmDelete = window.confirm(
      `Tem certeza que deseja excluir "${fileOrFolder.name}"?`
    );
  
    if (confirmDelete) {
      // Caminho completo para exclusão
      const fullPath = currentPath ? `${currentPath}/${fileOrFolder.name}` : fileOrFolder.name;
  
      api.post('/delete', { name: fullPath })
        .then(() => {
          fetchFiles(); // Atualiza a lista de arquivos após exclusão
        })
        .catch((error) => {
          console.error('Erro ao excluir item:', error);
        });
    }
  };
  

  const handleFileClick = (path) => {
    api.get(`/files/${path}`)
      .then((response) => {
        setCode(response.data.content); 
        setCurrentFile({ name: path });
      })
      .catch((error) => {
        console.error('Erro ao abrir arquivo:', error);
      });
  };

  const handleSearch = (query) => {
    setSearchQuery(query);
    if (!query) {
      setSearchResults(null);
      return;
    }

    api.get('/search', { params: { query } })
      .then((response) => {
        setSearchResults(response.data.results);
      })
      .catch((error) => {
        console.error('Erro ao buscar arquivos:', error);
      });
  };

  const renderItems = (items, depth = 0, currentPath = '') => {
    const itemsToRender = searchResults || items;
  
    return (
      <>
        {/* Identificador visual para a Root */}
        {depth === 0 && (
          <div
            className={`folder indent ${currentFolder === null ? 'selected' : ''}`}
            onClick={() => selectFolder(null)} // Define root como pasta selecionada
          >
            <FiFolder />
            {/* Espaço vazio para manter alinhamento */}
            <span style={{ visibility: 'hidden' }}>Root</span>
          </div>
        )}
  
        {itemsToRender.map((item) => {
          const fullPath = currentPath ? `${currentPath}/${item.name}` : item.name;
          const isRenaming = renaming === item.name;
  
          if (item.type === 'folder') {
            return (
              <div key={fullPath}>
                <div
                  className={`folder indent ${
                    currentFolder === fullPath ? 'selected' : ''
                  }`}
                  style={{ marginLeft: depth * 20 }}
                  onClick={(e) => {
                    e.stopPropagation(); // Evita conflitos com outros cliques
                    toggleFolder(fullPath);
                  }}
                  onDoubleClick={(e) => {
                    e.stopPropagation(); // Evita conflitos com outros eventos
                    selectFolder(fullPath);
                  }}
                >
                  {expandedFolders[fullPath] ? <FiChevronDown /> : <FiChevronRight />}
                  <FiFolder />
                  {isRenaming ? (
                    <div className="rename-actions">
                      <input
                        className="rename-input"
                        defaultValue={item.name}
                        onBlur={(e) => handleRename(item, e.target.value, currentPath)}
                        onKeyDown={(e) => {
                          if (e.key === 'Enter') handleRename(item, e.target.value, currentPath);
                          if (e.key === 'Escape') cancelRenaming();
                        }}
                        autoFocus
                      />
                      <button onClick={cancelRenaming}>Cancelar</button>
                    </div>
                  ) : (
                    <span>{item.name}</span>
                  )}
                  <div className="file-actions">
                    <button onClick={() => setRenaming(item.name)} title="Renomear">
                      <FiEdit />
                    </button>
                    <button onClick={() => handleDelete(item, currentPath)} title="Excluir">
                      <FiTrash />
                    </button>
                  </div>
                </div>
                {expandedFolders[fullPath] && (
                  <div>{renderItems(item.files || [], depth + 1, fullPath)}</div>
                )}
              </div>
            );
          }
  
          return (
            <div
              key={fullPath}
              className="file indent"
              style={{ marginLeft: depth * 20 }}
              onClick={() => handleFileClick(fullPath)}
            >
              <FiFile />
              {isRenaming ? (
                <div className="rename-actions">
                  <input
                    className="rename-input"
                    defaultValue={item.name}
                    onBlur={(e) => handleRename(item, e.target.value, currentPath)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleRename(item, e.target.value, currentPath);
                      if (e.key === 'Escape') cancelRenaming();
                    }}
                    autoFocus
                  />
                  <button onClick={cancelRenaming}>Cancelar</button>
                </div>
              ) : (
                <span>{item.name}</span>
              )}
              <div className="file-actions">
                <button onClick={() => setRenaming(item.name)} title="Renomear">
                  <FiEdit />
                </button>
                <button onClick={() => handleDelete(item, currentPath)} title="Excluir">
                  <FiTrash />
                </button>
              </div>
            </div>
          );
        })}
      </>
    );
  };

  if (loading) {
    return <div>Carregando arquivos...</div>;
  }

  return (
    <ExplorerContainer>
      {/* Barra de Pesquisa */}
      <div className="search-bar">
        <FiSearch />
        <input
          type="text"
          placeholder="Pesquisar arquivos ou pastas..."
          value={searchQuery}
          onChange={(e) => handleSearch(e.target.value)}
        />
      </div>
  
      <div className="actions">
        <button onClick={() => handleCreate(false)} title="Novo Arquivo">
          <FiPlus /> Novo Arquivo
        </button>
        <button onClick={() => handleCreate(true)} title="Nova Pasta">
          <FiPlus /> Nova Pasta
        </button>
      </div>
  
      {newItem && (
        <div className="new-item">
          <input
            type="text"
            placeholder={newItem.isFolder ? 'Nome da Pasta' : 'Nome do Arquivo'}
            value={newItem.name}
            onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
          />
          <button onClick={saveNewItem}>Salvar</button>
          <button onClick={cancelNewItem}>Cancelar</button>
        </div>
      )}
  
      {/* Renderiza os itens com ou sem filtro */}
      {renderItems(files)}
    </ExplorerContainer>
  );
}

export default FileExplorer;
