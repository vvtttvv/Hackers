import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import styles from './Right.module.css';


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

  const MarkdownWithCheckboxes = ({ text }) => (
    <ReactMarkdown
      children={text}
      remarkPlugins={[remarkGfm]}
      components={{
        // Custom renderer for text to add checkboxes before "*Step" or "**Step"
        text: ({ children }) => {
          const stepRegex = /(\*{1,2}Step\b)/g; // Matches "*Step" or "**Step"
          const parts = children[0].split(stepRegex);
  
          return (
            <>
              {parts.map((part, index) => (
                <React.Fragment key={index}>
                  {part.match(stepRegex) ? (
                    <>
                      <input type="checkbox" style={{ margin: '0 4px' }} />
                      {part}
                    </>
                  ) : (
                    part
                  )}
                </React.Fragment>
              ))}
            </>
          );
        },
      }}
    />
  );
  

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
              <MarkdownWithCheckboxes text={message.text} />
            ) : (
              message.text
            )}
          </div>
        ))}
      </div>

      {/* Input form */}
      <form className={styles.container} onSubmit={handleSubmit}>
        <div className={styles.inputWrapper}>
         
          <input
            type="text"
            className={styles.input}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="As dori sa..."
          
          />
        </div>
        <button type="submit" className={styles.button}>
          <img src='https://files.catbox.moe/ct7b3u.png' style={{ fontSize: '20px', margin: 'auto' }} />
        </button>
      </form>
    </div>
  );
}
