import React, { useState } from 'react';
import { ModalContainer, ModalContent, ModalActions } from './SaveFileModalStyles';

function SaveFileModal({ isOpen, onSave, onCancel, folders }) {
  const [fileName, setFileName] = useState('');
  const [selectedFolder, setSelectedFolder] = useState('');

  const handleSave = () => {
    if (!fileName.trim()) {
      alert('O nome do arquivo não pode estar vazio.');
      return;
    }
    onSave(fileName, selectedFolder);
  };

  if (!isOpen) return null;

  return (
    <ModalContainer>
      <ModalContent>
        <h3>Salvar Arquivo</h3>
        <input
          type="text"
          placeholder="Nome do arquivo"
          value={fileName}
          onChange={(e) => setFileName(e.target.value)}
        />
        <div>
          <label>Pasta:</label>
          <select
            value={selectedFolder}
            onChange={(e) => setSelectedFolder(e.target.value)}
          >
            <option value="">Pasta Raiz</option>
            {folders.map((folder) => (
              <option key={folder.name} value={folder.name}>
                {folder.name}
              </option>
            ))}
          </select>
        </div>
        <ModalActions>
          <button onClick={handleSave}>Salvar</button>
          <button onClick={onCancel}>Cancelar</button>
        </ModalActions>
      </ModalContent>
    </ModalContainer>
  );
}

export default SaveFileModal;
