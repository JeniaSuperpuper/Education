import logo from '../assets/images/logo.svg';
import RegistrationForm from './registration';
import Modal from './modal';
import { useState } from 'react';

export default function Header() {
    const [modalActive, setModalActive] = useState(false);

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
                        <button className='header__registration-sign' onClick={() => setModalActive(true)}>Sign Up</button>
                        <button className='header__registration-login' href="">Log in</button>
                    </div>
                </div>
            </div>
            <Modal active={modalActive} setActive={setModalActive}> <RegistrationForm/> </Modal>
        </header>
    );
}