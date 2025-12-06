// src/App.js

import React from 'react';
import Register from './components/Register';
import Login from './components/Login';

const App = () => {
    return (
        <div className="max-w-md mx-auto mt-10 p-4 bg-white shadow-md rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Frient Site Authorization</h1>
            <Register />
            <div className="divider my-4">If you have an account</div>
            <Login />
        </div>
    );
};

export default App;