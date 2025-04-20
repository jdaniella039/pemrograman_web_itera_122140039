import React from 'react';
import useBooks from '../hooks/useBooks';
import BookItem from './BookItem';

const BookList = ({ onEdit }) => {
  const { books, deleteBook } = useBooks();

  if (books.length === 0) return <p>Tidak ada buku.</p>;

  return (
    <div>
      {books.map((book) => (
        <BookItem key={book.id} book={book} onEdit={onEdit} onDelete={deleteBook} />
      ))}
    </div>
  );
};

export default BookList;