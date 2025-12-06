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
        <form onSubmit={handleLogin} className="container">
            <h2>Login</h2>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                required
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
            />
            <button type="submit">Login</button>
            {message && <p className={`message ${message.includes('successful') ? 'success' : 'error'}`}>{message}</p>}
        </form>
    );
};

export default Login;