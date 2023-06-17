import Gallery from '../components/Gallery';
import React from 'react';
import { createRoot } from 'react-dom/client';

const container = window.react_mount;
const root = createRoot(container); // createRoot(container!) if you use TypeScript
root.render(<Gallery />);