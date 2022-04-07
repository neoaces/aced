import React from 'react';
import * as ReactDOMClient from 'react-dom/client';
import './index.css';
import App from './App';

// 1. Element container of the react code <- HTML
// NOTE: the exclamation mark prevents the error saying that the 
// element returned might be null.
const container = document.getElementById('root')!

// 2. Create a root; React's way of rendering elements into HTML
const root = ReactDOMClient.createRoot(container) // <- ERROR RAISED HERE

// 3. Render the elements onto the root.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)