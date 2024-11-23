import styled from 'styled-components';

export const ExplorerContainer = styled.div`
  padding: 10px;
  font-family: 'Roboto', sans-serif;

  .folder, .file {
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

    &::before {
      content: '';
      position: absolute;
      left: ${(props) => (props.depth || 0) * 20}px;
      top: 50%;
      transform: translateY(-50%);
      width: 12px;
      height: 12px;
      background-color: ${({ theme }) => theme.colors.border};
      border-radius: 50%;
    }
  }

  .file {
    color: ${({ theme }) => theme.colors.text};

    &::before {
      content: '';
      position: absolute;
      left: ${(props) => (props.depth || 0) * 20}px;
      top: 50%;
      transform: translateY(-50%);
      width: 12px;
      height: 12px;
      background-color: ${({ theme }) => theme.colors.highlight};
      border-radius: 50%;
    }
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
