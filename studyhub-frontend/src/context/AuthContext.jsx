import { createContext, useContext, useState, useEffect, Children} from 'react';
import { jwtDecode } from 'jwt-decode';

const AuthContext = createContext();

export const AuthProvider = ({Children}) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem('token'));

    useEffect(() => {
        if (token){
            const decoded = jwtDecode(token);
            setUser(decoded);
        }
    }, [token])

    const login = (token) => {
        localStorage.setItem('token');
        setToken(token);
    };

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
        setToken(null);
    };

    return(
        <AuthContext.Provider value = {{user, token, login, logout}}>
            {Children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);