import styled from 'styled-components';

export const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
`;

export const Header = styled.header`
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: ${({ theme }) => theme.colors.header};
  color: ${({ theme }) => theme.colors.text};
  padding: 10px 20px;
  font-size: 1.2rem;
  font-weight: bold;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};
`;

export const MainContainer = styled.div`
  display: flex;
  flex-grow: 1;
  overflow: hidden;
`;

export const LeftPane = styled.div`
  width: 20%;
  border-right: 1px solid ${({ theme }) => theme.colors.border};
  background-color: ${({ theme }) => theme.colors.panel};
  overflow-y: auto;
`;

export const MiddlePane = styled.div`
  width: 50%;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
`;

export const RightPane = styled.div`
  width: 30%;
  border-left: 1px solid ${({ theme }) => theme.colors.border};
  background-color: ${({ theme }) => theme.colors.panel};
  overflow-y: auto;
`;

export const EditorHeader = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: ${({ theme }) => theme.colors.header};
  padding: 5px 10px; /* Reduzido para compactar o header */
  color: ${({ theme }) => theme.colors.text};
  font-weight: bold;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};

  .file-title {
    display: flex;
    align-items: center;
    background-color: ${({ theme }) => theme.colors.panel};
    padding: 3px 8px; /* Mais compacto verticalmente */
    border-radius: 4px; /* Bordas suaves */
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    font-size: 0.9rem;
    margin-bottom: -1px; /* Faz parecer que está "grudando" no editor */

    .close-button {
      margin-left: 8px; /* Ajustado para ficar mais próximo */
      background: none;
      border: none;
      color: ${({ theme }) => theme.colors.text};
      cursor: pointer;
      font-size: 1rem;

      &:hover {
        color: ${({ theme }) => theme.colors.error};
      }
    }
  }

  .action-buttons {
    display: flex;
    gap: 10px;

  button {
    background: none;
    border: none;
    color: ${({ theme }) => theme.colors.text};
    cursor: pointer;

    &:hover {
      color: ${({ theme }) => theme.colors.highlight};
    }
  }
`;

export const FooterContainer = styled.footer`
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: ${({ theme }) => theme.colors.header};
  color: ${({ theme }) => theme.colors.text};
  padding: 10px 20px;
  font-size: 0.9rem;
  border-top: 1px solid ${({ theme }) => theme.colors.border};
  flex-shrink: 0; /* Impede que o footer seja comprimido */
`;
