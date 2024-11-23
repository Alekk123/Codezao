import styled from 'styled-components';

export const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
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
`;

export const LeftPane = styled.div`
  width: 20%;
  border-right: 1px solid ${({ theme }) => theme.colors.border};
  background-color: ${({ theme }) => theme.colors.panel};
`;

export const MiddlePane = styled.div`
  width: 50%;
  display: flex;
  flex-direction: column;
`;

export const RightPane = styled.div`
  width: 30%;
  border-left: 1px solid ${({ theme }) => theme.colors.border};
  background-color: ${({ theme }) => theme.colors.panel};
`;

export const EditorHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: ${({ theme }) => theme.colors.header};
  padding: 10px;
  color: ${({ theme }) => theme.colors.text};
  font-weight: bold;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};

  button {
    background: none;
    border: none;
    color: ${({ theme }) => theme.colors.text};
    cursor: pointer;
    margin-left: 5px;

    &:hover {
      color: ${({ theme }) => theme.colors.highlight};
    }
  }
`;
