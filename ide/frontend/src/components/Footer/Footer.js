import React from 'react';
import { FooterContainer } from './FooterStyles';

function Footer({
  currentFile,
  connectionStatus,
  lastAction,
  toggleTheme,
  isDarkTheme,
}) {
  return (
    <FooterContainer status={connectionStatus}>
      {/* Informações do Arquivo e Conexão */}
      <div className="footer-left">
        <span>
          Arquivo: <strong>{currentFile?.name || 'Nenhum'}</strong>
        </span>
        <div className="status-indicator">
          <div className="status-circle" />
          <span>
            {connectionStatus === 'connected' ? 'Conectado' : 'Desconectado'}
          </span>
        </div>
      </div>

      {/* Alternância de Tema e Links */}
      <div className="footer-right">
        <div className="theme-switch">
          <span className="switch-label">Tema</span>
          <label className="switch">
            <input
              type="checkbox"
              checked={!isDarkTheme}
              onChange={toggleTheme}
            />
            <span className="slider" />
          </label>
        </div>
        <a href="#!" title="Documentação">
          Documentação
        </a>
        <a href="#!" title="Exemplos">
          Exemplos
        </a>
        <span>Codezão IDE - Criado com amor</span>
      </div>
    </FooterContainer>
  );
}

export default Footer;
