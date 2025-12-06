// src/api.js

import axios from 'axios';

const API_URL = 'http://localhost:8040/api/v1/auth';

export const registerUser = async (data) => {
    const response = await axios.post(`${API_URL}/register`, data);
    if (response.status === 200) {
        return response.data;
    }
    return "user is already registered";
};

export const loginUser = async (data) => {
    const response = await axios.post(`${API_URL}/login`, data);
    
    return response.data;
};