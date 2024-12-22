import React, { useState } from 'react';
import { useAuth } from './AuthContext';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:8000/api/v1/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        const data = await response.json();
        login(data); // Сохраняем токены
      } else {
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div>
      <h1 className='form__auth title'>Login</h1>
      <form className='form__auth form' onSubmit={handleSubmit}>
        <div className='form__auth div'>
          <label>
            <p>Email</p>
            <input
              className='form__auth input'
              type="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
        </div>
        <div className='form__auth div'>
          <label>
            <p>Password</p>
            <input
              className='form__auth input'
              type="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
        </div>
        <button className='form__auth button' type="submit">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginForm;