import styled from 'styled-components';

export const FooterContainer = styled.footer`
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: ${({ theme }) => theme.colors.header};
  color: ${({ theme }) => theme.colors.text};
  padding: 10px 20px;
  font-size: 0.9rem;
  border-top: 1px solid ${({ theme }) => theme.colors.border};
  flex-shrink: 0; /* Garante que o footer não encolha */
  

  .footer-left,
  .footer-right {
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .status-indicator {
    display: flex;
    align-items: center;
    gap: 5px;

    .status-circle {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: ${({ status, theme }) =>
        status === 'connected' ? theme.colors.highlight : theme.colors.error};
    }
  }

  .theme-switch {
    display: flex;
    align-items: center;
    cursor: pointer;

    .switch-label {
      margin-right: 10px;
    }

    .switch {
      position: relative;
      display: inline-block;
      width: 40px;
      height: 20px;

      input {
        opacity: 0;
        width: 0;
        height: 0;
      }

      .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: ${({ theme }) => theme.colors.border};
        border-radius: 20px;
        transition: 0.4s;

        &:before {
          position: absolute;
          content: '';
          height: 14px;
          width: 14px;
          left: 3px;
          bottom: 3px;
          background-color: ${({ theme }) => theme.colors.text};
          border-radius: 50%;
          transition: 0.4s;
        }
      }

      input:checked + .slider {
        background-color: ${({ theme }) => theme.colors.highlight};
      }

      input:checked + .slider:before {
        transform: translateX(20px);
      }
    }
  }
`;
