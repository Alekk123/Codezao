import styled from 'styled-components';

export const ExplorerContainer = styled.div`
  padding: 10px;
  font-family: 'Roboto', sans-serif;

  .actions {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;

    button {
      background: ${({ theme }) => theme.colors.panel};
      border: 1px solid ${({ theme }) => theme.colors.border};
      padding: 5px 10px;
      border-radius: 5px;
      color: ${({ theme }) => theme.colors.text};
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;

      &:hover {
        background: ${({ theme }) => theme.colors.highlight};
        color: #fff;
      }
    }
  }

  .new-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 5px;
    background: ${({ theme }) => theme.colors.panel};
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 5px;

    input {
      flex: 1;
      padding: 5px;
      border: 1px solid ${({ theme }) => theme.colors.border};
      border-radius: 5px;
      background: ${({ theme }) => theme.colors.background};
      color: ${({ theme }) => theme.colors.text};
    }

    button {
      padding: 5px 10px;
      border: none;
      background: ${({ theme }) => theme.colors.highlight};
      color: #fff;
      border-radius: 5px;
      cursor: pointer;

      &:hover {
        background: ${({ theme }) => theme.colors.text};
        color: ${({ theme }) => theme.colors.panel};
      }
    }
  }

  .rename-actions {
  display: flex;
  align-items: center;
  gap: 5px;

  input {
    flex: 1;
    margin-left: 5px;
    padding: 3px 5px;
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 3px;
    background-color: ${({ theme }) => theme.colors.panel};
    color: ${({ theme }) => theme.colors.text};
  }

  button {
    padding: 3px 10px;
    border: none;
    background: ${({ theme }) => theme.colors.error};
    color: #fff;
    border-radius: 3px;
    cursor: pointer;

    &:hover {
      background: ${({ theme }) => theme.colors.text};
      color: ${({ theme }) => theme.colors.panel};
    }
  }
}

  .folder,
  .file {
    display: flex;
    align-items: center;
    padding: 5px;
    cursor: pointer;
    position: relative;

    &:hover {
      background-color: ${({ theme }) => theme.colors.panel};
    }
  }

  .folder {
    font-weight: bold;
    color: ${({ theme }) => theme.colors.text};
  }

  .file {
    color: ${({ theme }) => theme.colors.text};
  }

  .indent {
    margin-left: ${(props) => (props.depth || 0) * 20}px;
  }

  .file-actions {
    margin-left: auto;
    display: flex;
    gap: 5px;
    visibility: hidden;
  }

  .file:hover .file-actions,
  .folder:hover .file-actions {
    visibility: visible;
  }

  .rename-input {
    flex: 1;
    margin-left: 5px;
    padding: 3px 5px;
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 3px;
    background-color: ${({ theme }) => theme.colors.panel};
    color: ${({ theme }) => theme.colors.text};
  }

  .rename-input:focus {
    outline: 1px solid ${({ theme }) => theme.colors.highlight};
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

  .file-actions button {
    background: none;
    border: none;
    color: ${({ theme }) => theme.colors.text};
    cursor: pointer;

    &:hover {
      color: ${({ theme }) => theme.colors.highlight};
    }
  }

  .search-bar {
  display: flex;
  align-items: center;
  background-color: ${({ theme }) => theme.colors.panel};
  padding: 5px;
  border-radius: 5px;
  margin-bottom: 10px;
  border: 1px solid ${({ theme }) => theme.colors.border};

  svg {
    margin-right: 5px;
    color: ${({ theme }) => theme.colors.text};
  }

  input {
    flex: 1;
    border: none;
    background: none;
    color: ${({ theme }) => theme.colors.text};
    outline: none;
    font-size: 0.9rem;
  }
}
`;

