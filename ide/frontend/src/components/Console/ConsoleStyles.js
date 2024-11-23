import styled from 'styled-components';

export const ConsoleContainer = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;

  .console-header {
    background-color: ${({ theme }) => theme.colors.header};
    color: ${({ theme }) => theme.colors.text};
    font-weight: bold;
    padding: 10px;
    border-bottom: 1px solid ${({ theme }) => theme.colors.border};
  }

  .console-output {
    background-color: ${({ theme }) => theme.colors.panel};
    color: ${({ theme }) => theme.colors.text};
    font-family: 'Courier New', monospace;
    padding: 10px;
    margin: 0;
    overflow-y: auto;
    flex-grow: 1; /* Permite que o console se expanda */
  }
`;
