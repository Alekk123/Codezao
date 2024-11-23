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

  useEffect(() => {
    fetchFiles();
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
    setNewItem({ isFolder, name: '' });
  };

  const saveNewItem = () => {
    if (!newItem.name.trim()) {
      alert('O nome não pode ser vazio.');
      return;
    }

    api.post('/create', {
      name: newItem.name,
      isFolder: newItem.isFolder,
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

  const handleRename = (fileOrFolder, newName) => {
    if (!newName.trim()) {
      cancelRenaming();
      return;
    }

    api.post('/rename', { oldName: fileOrFolder.name, newName })
      .then(() => {
        fetchFiles();
        setRenaming(null);
      })
      .catch((error) => {
        console.error('Erro ao renomear:', error);
      });
  };

  const cancelRenaming = () => {
    setRenaming(null);
  };

  const handleDelete = (fileOrFolder) => {
    const confirmDelete = window.confirm(
      `Tem certeza que deseja excluir "${fileOrFolder.name}"?`
    );

    if (confirmDelete) {
      api.post('/delete', { name: fileOrFolder.name })
        .then(() => {
          fetchFiles();
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
    // Use searchResults se a busca estiver ativa, caso contrário use items normalmente
    const itemsToRender = searchResults || items;
  
    return itemsToRender.map((item) => {
      const fullPath = currentPath ? `${currentPath}/${item.name}` : item.name;
      const isRenaming = renaming === item.name;
  
      if (item.type === 'folder') {
        return (
          <div key={fullPath}>
            <div
              className="folder indent"
              style={{ marginLeft: depth * 20 }}
              onClick={() => toggleFolder(fullPath)}
            >
              {expandedFolders[fullPath] ? <FiChevronDown /> : <FiChevronRight />}
              <FiFolder />
              {isRenaming ? (
                <div className="rename-actions">
                  <input
                    className="rename-input"
                    defaultValue={item.name}
                    onBlur={(e) => handleRename(item, e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleRename(item, e.target.value);
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
                <button onClick={() => handleDelete(item)} title="Excluir">
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
                onBlur={(e) => handleRename(item, e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') handleRename(item, e.target.value);
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
            <button onClick={() => handleDelete(item)} title="Excluir">
              <FiTrash />
            </button>
          </div>
        </div>
      );
    });
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
