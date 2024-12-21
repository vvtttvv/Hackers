import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import styles from './Right.module.css';
import imageSrc from '../../img/Снимок_экрана_2024-12-21_202107-removebg-preview.png';
import SendIcon from '@mui/icons-material/Send';

export default function Right() {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);
  const chatWindowRef = useRef(null);

  // Scroll to the latest message
  useEffect(() => {
    if (chatWindowRef.current) {
      chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return; // Prevent sending empty messages

    const userMessage = { text: inputValue, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInputValue('');

    try {
      const response = await fetch(
        `http://172.31.80.106:5000/api/kiki/?q=${encodeURIComponent(inputValue)}`,
        {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        }
      );

      if (response.ok) {
        const textResponse = await response.text();
        const serverMessage = {
          text: textResponse,
          sender: 'server',
          isMarkdown: true,
        };
        setMessages((prevMessages) => [...prevMessages, serverMessage]);
      } else {
        throw new Error('Ошибка отправки сообщения');
      }
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        text: error.message || 'Ошибка сети',
        sender: 'server',
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleSendMessage();
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className={styles.chatContainer}>
      {/* Chat messages display */}
      <div className={styles.chatWindow} ref={chatWindowRef}>
        {messages.map((message, index) => (
          <div
            key={index}
            className={`${styles.message} ${styles[message.sender]}`}
          >
            {message.isMarkdown ? (
              <ReactMarkdown>{message.text}</ReactMarkdown>
            ) : (
              message.text
            )}
          </div>
        ))}
      </div>

      {/* Input form */}
      <form className={styles.container} onSubmit={handleSubmit}>
        <div className={styles.inputWrapper}>
          <img
            src={imageSrc}
            alt="Новогоднее изображение"
            className={styles.image}
          />
          <input
            type="text"
            className={styles.input}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Введите сообщение"
          />
        </div>
        <button type="submit" className={styles.button}>
          <SendIcon style={{ fontSize: '20px', margin: 'auto' }} />
        </button>
      </form>
    </div>
  );
}
