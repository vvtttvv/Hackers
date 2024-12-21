import styles from './App.module.css'
import Header from './features/Header/header'
import ClientPage from './Pages/ClientPage';
import AdminPage from './Pages/AdminPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {

  return (
    <div className={styles.wrapper}>
      <Router>
        <div className={styles.header}>
          <Header/>
        </div>
        <div className={styles.footer}>
          <Routes>
            <Route path="/admin" element={<AdminPage />} />
            <Route path="/client" element={<ClientPage />} />
          </Routes>
        </div>
      </Router>
    </div>
  )
}

export default App
