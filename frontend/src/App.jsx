import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header.jsx';
import Main from './components/MainSection.jsx';
import Catalog from './components/CatalogSection.jsx';
import CatalogSearch from './components/CatalogSearch.jsx';
import { AuthProvider } from './components/AuthContext.jsx';
import VerifyEmail from './components/VerifyEmail.jsx';

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <Header />
        <Routes>
          <Route path="/verify-email/:userId/:token/" element={<VerifyEmail />} />
          <Route path="/" element={<Main />} />
          <Route path="/catalog" element={<Catalog />}/>
        </Routes>
      </Router>
    </AuthProvider>
  );
}