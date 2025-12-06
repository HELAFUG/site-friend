// src/components/Login.js

import React, { useState } from 'react';
import { loginUser } from '../api';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await loginUser({ email, password });
            setMessage(`Login successful: ${response.message}`);
        } catch (error) {
            console.error('Error during login:', error);
            setMessage('Login failed. Please try again.');
        }
    };

    return (
        <form onSubmit={handleLogin} className="space-y-4">
            <h2 className="text-lg font-bold">Login</h2>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                required
                className="border p-2 w-full"
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
                className="border p-2 w-full"
            />
            <button type="submit" className="bg-blue-500 text-white p-2 rounded">Login</button>
            {message && <p>{message}</p>}
        </form>
    );
};

export default Login;