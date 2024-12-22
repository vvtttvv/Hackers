import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import styles from './Left.module.css';

export default function DocumentsTable() {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    /*fetch('http://172.31.80.106:5000/api/documents')
      .then((response) => response.json())
      .then((data) => {
        setDocuments(data);
      })
      .catch((error) => console.error('Error fetching data:', error));*/
  }, []);

  return (
    <div className={styles.wrapper}>
      <TableContainer
  component={Paper}
  sx={{
    backgroundColor: '#2C3E50',
    padding: '16px',
    borderRadius: '12px',
    margin: '16px auto',
    maxWidth: '95%',
    maxHeight: '600px',
    overflowY: 'auto',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    '&::-webkit-scrollbar': {
      width: '2px', // уменьшил с 4px до 2px
      height: '2px',
    },
    '&::-webkit-scrollbar-track': {
      background: 'transparent',
      margin: '4px 0', // добавил отступы сверху и снизу
    },
    '&::-webkit-scrollbar-thumb': {
      background: 'rgba(149, 165, 166, 0.3)', // сделал более прозрачным
      borderRadius: '4px', // увеличил радиус закругления
      '&:hover': {
        background: 'rgba(149, 165, 166, 0.5)', // уменьшил непрозрачность при наведении
        transition: 'background-color 0.2s ease', // добавил плавное изменение цвета
      },
    },
    // Добавил стили для Firefox
    scrollbarWidth: 'thin',
    scrollbarColor: 'rgba(149, 165, 166, 0.3) transparent',
  }}
>
        <Table stickyHeader>
          <TableHead>
            <TableRow>
              {['Issued By', 'Issued On', 'Due Date', 'Product', 'Email', 'Quantity', 'Unit Price', 'Subtotal', 'TVA', 'Total', 'Bank Name'].map((header) => (
                <TableCell
                  key={header}
                  sx={{
                    backgroundColor: '#34495E',
                    color: '#ECF0F1',
                    fontSize: '0.57rem',
                    fontWeight: 'bold',
                    padding: '12px 16px',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {header}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {documents.map((doc, index) => (
              <TableRow
                key={index}
                sx={{
                  '&:nth-of-type(odd)': {
                    backgroundColor: 'rgba(236, 240, 241, 0.05)',
                  },
                  '&:hover': {
                    backgroundColor: 'rgba(236, 240, 241, 0.1)',
                  },
                  transition: 'background-color 0.2s ease',
                }}
              >
                {Object.values(doc).map((value, cellIndex) => (
                  <TableCell
                    key={cellIndex}
                    sx={{
                      color: '#ECF0F1',
                      fontSize: '0.57rem',
                      padding: '8px 16px',
                      borderBottom: '1px solid rgba(236, 240, 241, 0.1)',
                    }}
                  >
                    {value}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}