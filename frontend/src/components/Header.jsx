import React, { useState } from 'react';
import logo from '../assets/images/logo.svg';
import RegistrationForm from './registration';
import AuthForm from './login';
import Modal from './modal';
import { useAuth } from './AuthContext';

export default function Header() {
  const [modalActive, setModalActive] = useState(false);
  const [modalActiveLogin, setModalActiveLogin] = useState(false);
  const { user, logout } = useAuth();

  return (
    <header className="header">
      <div className="container">
        <div className="header__wrapper">
          <div className="header__logo">
            <img src={logo} alt="logo" />
            <h1>Edudu</h1>
          </div>
          <ul className="header__navigation">
            <li><button href="#">Course</button></li>
            <li><button href="#">Teacher</button></li>
            <li><button href="#">How to use</button></li>
            <li><button href="#">About Us</button></li>
          </ul>
          <div className="header__registration">
            {user ? (
              <button className='header__registration-logout' onClick={logout}>Logout</button>
            ) : (
              <>
                <button className='header__registration-sign' onClick={() => setModalActive(true)}>Sign Up</button>
                <button className='header__registration-login' onClick={() => setModalActiveLogin(true)}>Log in</button>
              </>
            )}
          </div>
        </div>
      </div>
      <Modal active={modalActive} setActive={setModalActive}> <RegistrationForm /> </Modal>
      <Modal active={modalActiveLogin} setActive={setModalActiveLogin}> <AuthForm /> </Modal>
    </header>
  );
}