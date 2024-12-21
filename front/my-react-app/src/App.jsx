import { useState } from 'react'
import styles from './App.module.css'

function App() {

  return (
    <div className={styles.wrapper}>
      <div className={styles.firstBlock}>
        First block
      </div>
      <div className={styles.secondBlock}>
        Second block
      </div>
    </div>
  )
}

export default App
