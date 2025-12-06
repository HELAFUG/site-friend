// src/components/Register.js

import React, { useState } from 'react';
import { registerUser } from '../api';

const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await registerUser({ email, password });
            setMessage(`Registration successful: ${response.message}`);
            if (response.status === 400) {
                setMessage(response.message);
                
            }
        } catch (error) {
            console.error('Error during registration:', error);
            setMessage('Registration failed. Please try again.');
        }
    };

    return (
        <form onSubmit={handleRegister} className="container">
            <h2>Register</h2>
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
            <button type="submit">Register</button>
            {message && <p className={`message ${message.includes('successful') ? 'success' : 'error'}`}>{message}</p>}
        </form>
    );
};

export default Register;