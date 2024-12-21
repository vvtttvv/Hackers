import { Link } from 'react-router-dom';
import styles from './header.module.css';

export default function Header() {
  return (
    <div className={styles.wrapper}>
      <nav>
        <Link to="/admin" className={styles.link}>Admin Page</Link>
        <Link to="/client" className={styles.link}>Client Page</Link>
      </nav>
    </div>
  );
}
