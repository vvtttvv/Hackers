import styles from './AdminPage.module.css'
import Left from '../features/Left/left'
import CollapsibleTable from '../features/right/Right'
import SnowfallCanvas from './SnowFall'

export default function AdminPage() {

  

  return (
    <div className={styles.wrapper}>
      <SnowfallCanvas/>
      <div className={styles.firstBlock}>
        <Left />
      </div>
      <div className={styles.secondBlock}>
        <CollapsibleTable />
      </div>
    </div>
  )
}
