import React from 'react';
import { ConsoleContainer } from './ConsoleStyles';

function Console({ output }) {
  return (
    <ConsoleContainer>
      <div className="console-header">Console</div>
      <pre className="console-output">{output}</pre>
    </ConsoleContainer>
  );
}

export default Console;
