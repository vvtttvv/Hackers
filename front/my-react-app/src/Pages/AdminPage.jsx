import styles from './AdminPage.module.css'
import Left from '../features/Left/left'

export default function AdminPage() {

  return (
    <div className={styles.wrapper}>
      <div className={styles.firstBlock}>
        <Left />
      </div>
      <div className={styles.secondBlock}>
        Second block
      </div>
    </div>
  )
}
