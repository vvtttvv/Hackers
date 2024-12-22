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
    fetch('http://172.31.80.106:5000/api/documents')
      .then((response) => response.json())
      .then((data) => {
        setDocuments(data);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className={styles.wrapper}>
   
        <Table stickyHeader sx={{ fontFamily: 'DotGothic16, serif', maxHeight: '490px', minHeight: '490px'}}>
          <TableHead>
            <TableRow>
              {['Issued By', 'Issued On', 'Due Date', 'Product', 'Email', 'Quantity', 'Unit Price', 'Subtotal', 'TVA', 'Total', 'Bank Name'].map((header) => (
                <TableCell
                  key={header}
                  sx={{
                    backgroundColor: '#D4D0C8',
                    color: '#000',
                    fontSize: '0.57rem',
                    fontWeight: 'bold',
                    padding: '12px 16px',
                    whiteSpace: 'nowrap',
                    fontFamily: 'DotGothic16, serif', // Force font for the header
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
                    backgroundColor: '#d9b8b8',
                  },
                  '&:hover': {
                    backgroundColor: 'rgb(159, 202, 213)',
                  },
                  transition: 'background-color 0.2s ease',
                  fontFamily: 'DotGothic16, serif', // Apply font for rows
                }}
              >
                {Object.values(doc).map((value, cellIndex) => (
                  <TableCell
                    key={cellIndex}
                    sx={{
                      color: '#000',
                      fontSize: '0.57rem',
                      padding: '8px 16px',
                      borderBottom: '1px solid rgba(229, 231, 166, 0.1)',
                      fontFamily: 'DotGothic16, serif', // Apply font for cells
                    }}
                  >
                    {value}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      
    </div>
  );
}