import { useState } from 'react'
import styles from './Left.module.css'

export default function Left() {

  return (
    <div className={styles.wrapper}>
        <div className={styles.statistic}>
          <span class="material-symbols-outlined">home</span>
          <p>5k+</p>
          <div className={styles.line}></div>
          <p> $15000 </p>
        </div>

        <div className={styles.messages}>
          Here are messages
        </div>
    </div>
  )
}

