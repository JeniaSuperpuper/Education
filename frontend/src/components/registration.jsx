import React, { useState } from 'react';

export default function RegistrationForm() {
  // Состояние для хранения данных формы
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirm_password: '',
  });

  // Состояние для отображения сообщений об ошибках или успехе
  const [message, setMessage] = useState('');

  // Обработчик изменения полей формы
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Обработчик отправки формы
  const handleSubmit = async (e) => {
    e.preventDefault(); // Предотвращаем перезагрузку страницы

    // Проверка на совпадение паролей
    if (formData.password !== formData.confirm_password) {
      setMessage('Пароли не совпадают');
      return;
    }

    try {
      // Отправка данных на сервер с помощью fetch
      const response = await fetch('http://127.0.0.1:8000/api/v1/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData), // Преобразуем данные в JSON
      });

      // Обработка ответа от сервера
      const data = await response.json();
      if (response.ok) {
        setMessage('Регистрация прошла успешно!');
        // Очищаем форму после успешной отправки
        setFormData({
          username: '',
          email: '',
          password: '',
          confirm_password: '',
        });
      } else {
        setMessage(`Ошибка: ${data.message}`);
      }
    } catch (error) {
      setMessage('Произошла ошибка при отправке данных');
    }
  };

  return (
    <div>
      <h1 className='form__auth title'>Регистрация</h1>
      <form className='form__auth form' onSubmit={handleSubmit}>
        <div className='form__auth div'>
            <label>
            <p>Username</p>
            <input className='form__auth input'
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
            />
            </label>
        </div>
        <div className='form__auth div'>
            <label>
            <p>Email</p>
            <input className='form__auth input'
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
            </label>
        </div>
        <div className='form__auth div'>
            <label>
            <p>Password</p>
            <input className='form__auth input'
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
            </label>
        </div>
        <div className='form__auth div'>
            <label>
            <p>Confirm password</p>
            <input className='form__auth input'
              type="password"
              name="confirm_password"
              value={formData.confirm_password}
              onChange={handleChange}
              required
            />
            </label>
        </div>
        {message && <p className='form__auth info'>{message}</p>}
        <button className='form__auth button' type="submit">Зарегистрироваться</button>
      </form>
    </div>
  );
}
