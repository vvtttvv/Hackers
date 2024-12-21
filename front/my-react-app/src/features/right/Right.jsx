import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import styles from './Right.module.css';
import imageSrc from '../../img/Снимок_экрана_2024-12-21_202107-removebg-preview.png';

export default function Right() {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const newMessage = { text: inputValue, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInputValue('');

    try {
      const response = await fetch(`http://172.31.80.106:5000/api/kiki/?q=${encodeURIComponent(inputValue)}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (response.ok) {
        const textResponse = await response.text(); // Use text(), not json()
        const serverMessage = { text: textResponse, sender: 'server', isMarkdown: true }; // Add Markdown flag
        setMessages((prevMessages) => [...prevMessages, serverMessage]);
      } else {
        const errorMessage = { text: 'Ошибка отправки сообщения', sender: 'server' };
        setMessages((prevMessages) => [...prevMessages, errorMessage]);
      }
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = { text: 'Ошибка сети', sender: 'server' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatWindow}>
        {messages.map((message, index) => (
          <div key={index} className={`${styles.message} ${styles[message.sender]}`}>
            {message.isMarkdown ? (
              <ReactMarkdown>{message.text}</ReactMarkdown> // Render Markdown
            ) : (
              message.text
            )}
          </div>
        ))}
      </div>

      <form className={styles.container} onSubmit={handleSubmit}>
        <div className={styles.inputWrapper}>
          <img src={imageSrc} alt="Новогоднее изображение" className={styles.image} />
          <input
            type="text"
            className={styles.input}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Введите сообщение"
          />
        </div>
        <button type="submit" className={styles.button}>
          Отправить
        </button>
      </form>
    </div>
  );
}





