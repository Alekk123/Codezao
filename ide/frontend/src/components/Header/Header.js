// src/components/Header/Header.js
import React from 'react';
import styled from 'styled-components';
import { FiFolderPlus } from 'react-icons/fi';

const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: ${({ theme }) => theme.colors.header};
  color: ${({ theme }) => theme.colors.text};
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};
`;

const Title = styled.h1`
  font-size: 1.5rem;
  margin: 0;
`;

const Actions = styled.div`
  display: flex;
  gap: 15px;

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

function Header({ onCreateFile }) {
  return (
    <HeaderContainer>
      <Title>Codezão IDE</Title>
      <Actions>
        <button onClick={onCreateFile} title="Criar Novo Arquivo">
          <FiFolderPlus size={20} />
        </button>
      </Actions>
    </HeaderContainer>
  );
}

export default Header;
