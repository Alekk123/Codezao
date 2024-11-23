import styled from 'styled-components';

export const ExplorerContainer = styled.div`
  .folder, .file {
    padding: 5px;
    margin-left: 10px;
    cursor: pointer;
    display: flex;
    align-items: center;

    &:hover {
      background-color: ${({ theme }) => theme.colors.panel};
    }
  }

  .file-actions {
    margin-left: auto;
    display: flex;
    gap: 5px;
    visibility: hidden;
  }

  .file:hover .file-actions, .folder:hover .file-actions {
    visibility: visible;
  }

  .rename-input {
    flex: 1;
    margin-left: 5px;
    border: none;
    background-color: ${({ theme }) => theme.colors.panel};
    color: ${({ theme }) => theme.colors.text};
  }

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
