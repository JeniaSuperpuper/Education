import './App.css'
import Header from './components/Header.jsx'
import Main from './components/MainSection.jsx'
import { AuthProvider } from './components/AuthContext.jsx'
import Catalog from './components/CatalogSection.jsx'


export default function App() {
  return (
    <AuthProvider>
      <Header />
      <Main/>
      <Catalog/>
    </AuthProvider>
  )
}

