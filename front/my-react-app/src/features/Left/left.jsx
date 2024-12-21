import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import styles from'./Left.module.css'

export default function DocumentsTable() {
  const [documents, setDocuments] = useState([]);

    useEffect(() => {
      fetch('http://172.31.80.106:5000/api/documents')
        .then(response => response.json())
        .then(data => {
          setDocuments(data);
        })
        .catch(error => console.error('Error fetching data:', error));
    }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.statistic}>
        <span className="material-symbols-outlined">home</span>
        <p>0+</p>
        <div className={styles.line}></div>
        <p>5</p>
      </div>
        
      <TableContainer
        component={Paper}
        sx={{
          backgroundColor: '#BCB8B1',
          padding: '16px',
          borderRadius: '8px',
          margin: '16px auto',
          maxWidth: '90%',
        }}
      >
      <Table>
        <TableHead>
          <TableRow>
            <TableCell sx={{ color: 'white' }}>Bank Name</TableCell>
            <TableCell sx={{ color: 'white' }}>Due Date</TableCell>
            <TableCell sx={{ color: 'white' }}>Email</TableCell>
            <TableCell sx={{ color: 'white' }}>Issued By</TableCell>
            <TableCell sx={{ color: 'white' }}>Product</TableCell>
            <TableCell sx={{ color: 'white' }}>Quantity</TableCell>
            <TableCell sx={{ color: 'white' }}>Total</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {documents.map((doc, index) => (
            <TableRow key={index}>
              <TableCell sx={{ color: 'white' }}>{doc.bank_name}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.due_date}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.email}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.issued_by}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.product}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.quantity}</TableCell>
              <TableCell sx={{ color: 'white' }}>{doc.total}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      </TableContainer>
    </div>
  );
}
