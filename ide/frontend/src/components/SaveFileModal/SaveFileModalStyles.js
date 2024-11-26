import styled from 'styled-components';

export const ModalContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
`;

export const ModalContent = styled.div`
  background: ${({ theme }) => theme.colors.panel};
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  color: ${({ theme }) => theme.colors.text};
  min-width: 300px;

  .folder-list {
    max-height: 200px;
    overflow-y: auto;
    margin-bottom: 20px; /* Espaçamento extra antes dos botões */
  }

  .modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px; /* Espaçamento entre os botões */
  }

  h3 {
    margin-bottom: 15px;
  }

  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 4px;
    background: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.text};
  }

  select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 15px;
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 4px;
    background: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.text};
  }
`;

export const ModalActions = styled.div`
  display: flex;
  gap: 10px;

  button {
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    background: ${({ theme }) => theme.colors.highlight};
    color: #fff;

    &:hover {
      background: ${({ theme }) => theme.colors.text};
      color: ${({ theme }) => theme.colors.panel};
    }
  }
`;
