import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Восстанавливаем состояние из localStorage при загрузке
  useEffect(() => {
    const authTokens = JSON.parse(localStorage.getItem('authTokens'));
    if (authTokens) {
      setUser(authTokens);
    }
  }, []);

  const login = (data) => {
    setUser(data);
    localStorage.setItem('authTokens', JSON.stringify(data));
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('authTokens');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};