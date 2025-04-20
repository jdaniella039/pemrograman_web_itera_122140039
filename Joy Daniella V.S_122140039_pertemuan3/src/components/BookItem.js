import React from 'react';

const BookItem = ({ book, onEdit, onDelete }) => (
  <div>
    <h3>{book.title}</h3>
    <p>{book.author}</p>
    <button onClick={() => onEdit(book)}>Edit</button>
    <button onClick={() => onDelete(book.id)}>Hapus</button>
  </div>
);

export default BookItem;