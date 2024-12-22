import styles from './header.module.css';

export default function Header() {
  return (
    <div className={styles.Header}>
      <div className={styles.button}>
        <img className={styles.image} src="./src/img/images.png" alt="Something went wrong" />
      </div>
      <div className={styles.cattttt}>
        <img className={`${styles.image} ${styles.cat}`} src="./src/img/cat.png" alt="Something went wrong" />
      </div>

      <div className={styles.another_img}>
        <img className={styles.image} src="./src/img/images-removebg-preview.png" alt="Something went wrong" />
      </div>
    </div>
  );
}
