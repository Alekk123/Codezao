import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    background-color: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.text};
    font-family: 'Roboto', sans-serif;
    height: 100%; /* Garante que o body ocupe exatamente a altura */
    overflow: hidden; /* Evita elementos extras rolando abaixo do footer */
  }

  #root {
    display: flex;
    flex-direction: column;
    height: 100vh; /* Garante que o root ocupe toda a janela */
    overflow: hidden; /* Bloqueia transbordo do conteúdo */
  }

  * {
    box-sizing: border-box;
  }

  .app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }

  .app-body {
    display: flex;
    height: 100%;
  }

  .left-pane, .middle-pane, .right-pane {
    overflow-y: auto;
  }

  .left-pane {
    background-color: ${({ theme }) => theme.colors.panel};
    width: 20%;
    border-right: 1px solid ${({ theme }) => theme.colors.border};
    padding: 10px;
  }

  .middle-pane {
    background-color: ${({ theme }) => theme.colors.panel};
    width: 50%;
    display: flex;
    flex-direction: column;
  }

  .right-pane {
    background-color: ${({ theme }) => theme.colors.panel};
    width: 30%;
    border-left: 1px solid ${({ theme }) => theme.colors.border};
    padding: 10px;
  }

  .editor-header, .console-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: ${({ theme }) => theme.colors.header};
    padding: 10px;
    color: ${({ theme }) => theme.colors.text};
    font-weight: bold;
    border-bottom: 1px solid ${({ theme }) => theme.colors.border};
  }
`;

export default GlobalStyles;
