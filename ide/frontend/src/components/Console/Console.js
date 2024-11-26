import React from 'react';
import { FiTrash } from 'react-icons/fi';
import { ConsoleContainer } from './ConsoleStyles';

function Console({ output, clearOutput }) {
  return (
    <ConsoleContainer>
      <div className="console-header">
        Console
        <FiTrash
          className="clear-icon"
          onClick={clearOutput}
          title="Limpar Console"
          size={20}
        />
      </div>
      <pre className="console-output">{output}</pre>
    </ConsoleContainer>
  );
}

export default Console;
