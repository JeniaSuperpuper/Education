import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';

const VerifyEmail = () => {
  const { userId, token } = useParams();
  const [message, setMessage] = useState(''); // Состояние для хранения сообщения
  const [isLoading, setIsLoading] = useState(true); // Состояние для индикации загрузки

  useEffect(() => {
    const verifyEmail = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/api/v1/users/verify-email/${userId}/${token}/`,
          {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );

        const data = await response.json(); // Парсим JSON из ответа

        if (response.ok) {
          setMessage(data.detail || 'Email verification successful'); // Используем поле detail
        } else {
          setMessage(data.detail || 'Email verification failed'); // Используем поле detail
        }
      } catch (error) {
        setMessage('Error during email verification');
        console.error('Error during email verification:', error);
      } finally {
        setIsLoading(false); // Завершаем загрузку
      }
    };

    verifyEmail();
  }, [userId, token]);

  return (
    <div>
      {isLoading ? (
        <h1 className='verify__title'>Verifying your email...</h1>
      ) : (
        <div className='verify'>
          <h1 verify__title>{message}</h1>
          <Link to='/' className='verify__backBtn'>Back</Link>
        </div>
      )}
    </div>
  );
};

export default VerifyEmail;