// src/App.js

import React from 'react';
import Register from './components/Register';
import Login from './components/Login';

const App = () => {
    return (
        <div className="max-w-md mx-auto mt-10 p-4 bg-white shadow-md rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Auth App</h1>
            <Register />
            <div className="divider my-4">OR</div>
            <Login />
        </div>
    );
};

export default App;