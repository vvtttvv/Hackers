import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import styles from './Left.module.css';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';

export default function DocumentsTable() {
  const [documents, setDocuments] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    fetch('http://172.31.80.106:5000/api/documents')
      .then((response) => response.json())
      .then((data) => {
        setDocuments(data);
        console.log(data);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const handleClickOpen = (doc) => {
    setSelectedDoc(doc);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setSelectedDoc(null);
  };

  const handleRowClick = (event, doc) => {
    if (event.target.type === 'checkbox') {
      return;
    }
    // Assuming doc.url contains the relative PDF path like 'attachments/invoice-2.pdf'
    const pdfUrl = `http://172.31.80.106:5000/${doc.url}`;
    setSelectedDoc({ ...doc, pdfUrl });
    setOpen(true);
  };

  return (
    <div className={styles.wrapper}>
      <Table stickyHeader sx={{ fontFamily: 'DotGothic16, serif', maxHeight: '490px', minHeight: '490px' }}>
        <TableHead>
          <TableRow>
            {['Due Date', 'Issued By', 'Issued On', 'Product', 'Quantity', 'Subtotal', 'Total', 'TVA', 'Unit Price'].map((header) => (
              <TableCell
                key={header}
                sx={{
                  backgroundColor: '#D4D0C8',
                  color: '#000',
                  fontSize: '0.57rem',
                  fontWeight: 'bold',
                  padding: '12px 16px',
                  whiteSpace: 'nowrap',
                  fontFamily: 'DotGothic16, serif',
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
              onClick={(event) => handleRowClick(event, doc)}
              sx={{
                '&:nth-of-type(odd)': {
                  backgroundColor: '#d9b8b8',
                },
                '&:hover': {
                  backgroundColor: 'rgb(159, 202, 213)',
                },
                transition: 'background-color 0.2s ease',
                fontFamily: 'DotGothic16, serif',
              }}
            >
              {Object.values(doc).map((value, cellIndex) => (
                (cellIndex === 1) || (cellIndex === 10)  ? (
                  <></>
                ) : (
                  <TableCell
                    key={cellIndex}
                    sx={{
                      color: '#000',
                      fontSize: '0.57rem',
                      padding: '8px 16px',
                      borderBottom: '1px solid rgba(229, 231, 166, 0.1)',
                      fontFamily: 'DotGothic16, serif',
                    }}
                  >
                    {value}
                  </TableCell>
                )
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Dialog open={open} onClose={handleClose} maxWidth="md" fullWidth>
        <DialogTitle sx={{ fontFamily: 'DotGothic16, serif' }}>
          Invoice Details
        </DialogTitle>
        <DialogContent>
          {selectedDoc && (
            <div style={{ fontFamily: 'DotGothic16, serif' }}>
              {selectedDoc.pdfUrl ? (
                <iframe
                  src={selectedDoc.pdfUrl}
                  width="100%"
                  height="400px"
                  style={{ border: 'none' }}
                />
              ) : (
                Object.entries(selectedDoc).map(([key, value]) => (
                  <div key={key} style={{ margin: '10px 0' }}>
                    <strong>{key}:</strong> {value}
                  </div>
                ))
              )}
            </div>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} sx={{ fontFamily: 'DotGothic16, serif' }}>
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
