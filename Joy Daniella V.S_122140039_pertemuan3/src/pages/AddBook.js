import React from 'react';
import BookForm from '../components/BookForm';
import useBooks from '../hooks/useBooks';

const AddBook = () => {
  const { addBook } = useBooks();

  return <BookForm onSubmit={addBook} />;
};

export default AddBook;