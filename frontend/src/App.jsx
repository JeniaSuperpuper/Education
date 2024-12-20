import './App.css'

function Header() {
  return(
    <header>
      <h3>Logo</h3>
      <h3>Navigation</h3>
      <h3>Login</h3>
    </header>
  )
}

let now = new Date()

export default function App() {
  return (
    <div>
      <Header />
      <main>
        <h1>time: {now.toLocaleTimeString()}</h1>
      </main>
    </div>
  )
}

