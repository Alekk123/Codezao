import React, { useState, useEffect } from 'react';
import api from '../../utils/api';
import {
  FiFolder,
  FiFolderPlus,
  FiFile,
  FiFilePlus,
  FiChevronDown,
  FiChevronRight,
  FiEdit,
} from 'react-icons/fi';
import { ExplorerContainer } from './FileExplorerStyles';

function FileExplorer({ setCode, setCurrentFile }) {
  const [files, setFiles] = useState([]);
  const [expandedFolders, setExpandedFolders] = useState({});
  const [loading, setLoading] = useState(true);
  const [renaming, setRenaming] = useState(null);

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

  const handleRename = (fileOrFolder, newName) => {
    if (!newName.trim()) return;

    api.post('/rename', { oldName: fileOrFolder.name, newName })
      .then(() => {
        fetchFiles();
        setRenaming(null);
      })
      .catch((error) => {
        console.error('Erro ao renomear:', error);
      });
  };

  const toggleFolder = (folderName) => {
    setExpandedFolders((prev) => ({
      ...prev,
      [folderName]: !prev[folderName],
    }));
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

  const renderItems = (items, currentPath = '') => {
    return items.map((item) => {
      const fullPath = currentPath ? `${currentPath}/${item.name}` : item.name;
      const isRenaming = renaming === item.name;

      if (item.type === 'folder') {
        return (
          <div key={fullPath}>
            <div className="folder" onClick={() => toggleFolder(fullPath)}>
              {expandedFolders[fullPath] ? <FiChevronDown /> : <FiChevronRight />}
              <FiFolder />
              {isRenaming ? (
                <input
                  className="rename-input"
                  defaultValue={item.name}
                  onBlur={(e) => handleRename(item, e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter') handleRename(item, e.target.value);
                    if (e.key === 'Escape') setRenaming(null);
                  }}
                  autoFocus
                />
              ) : (
                <span onDoubleClick={() => setRenaming(item.name)}>{item.name}</span>
              )}
              <div className="file-actions">
                <button onClick={() => setRenaming(item.name)} title="Renomear">
                  <FiEdit />
                </button>
              </div>
            </div>
            {expandedFolders[fullPath] && <div>{renderItems(item.files, fullPath)}</div>}
          </div>
        );
      }

      return (
        <div
          key={fullPath}
          className="file"
          onClick={() => handleFileClick(fullPath)}
        >
          <FiFile />
          {isRenaming ? (
            <input
              className="rename-input"
              defaultValue={item.name}
              onBlur={(e) => handleRename(item, e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter') handleRename(item, e.target.value);
                if (e.key === 'Escape') setRenaming(null);
              }}
              autoFocus
            />
          ) : (
            <span>{item.name}</span>
          )}
          <div className="file-actions">
            <button onClick={() => setRenaming(item.name)} title="Renomear">
              <FiEdit />
            </button>
          </div>
        </div>
      );
    });
  };

  if (loading) {
    return <div>Carregando arquivos...</div>;
  }

  return <ExplorerContainer>{renderItems(files)}</ExplorerContainer>;
}

export default FileExplorer;
