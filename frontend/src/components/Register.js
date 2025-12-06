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
        } catch (error) {
            console.error('Error during registration:', error);
            setMessage('Registration failed. Please try again.');
        }
    };

    return (
        <form onSubmit={handleRegister} className="space-y-4">
            <h2 className="text-lg font-bold">Register</h2>
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
            <button type="submit" className="bg-blue-500 text-white p-2 rounded">Register</button>
            {message && <p>{message}</p>}
        </form>
    );
};

export default Register;