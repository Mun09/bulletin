import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Chat from './components/Bulletin/Bulletin'

const App = () => (
    <Router>
        <Routes>
            <Route path="/" exact element={<Chat/>} />
        </Routes>
    </Router>
)

export default App;
