import React from 'react';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home';

function App() {
  return (
    <BookProvider>
      <Home />
    </BookProvider>
  );
}

export default App;