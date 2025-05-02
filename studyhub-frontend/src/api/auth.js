import axios from 'axios';

const API = 'http://localhost:8000/api';

export const loginUser = async (email, password) => {
    const response = await axios.post('${API}/token/', {
        email,
        password,
    });

    return response.data.access;
};