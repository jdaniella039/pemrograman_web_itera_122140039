import { useContext } from 'react';
import { BookContext } from '../context/BookContext';

const useBooks = () => {
  const { books, setBooks } = useContext(BookContext);

  const addBook = (book) => {
    setBooks([...books, { ...book, id: Date.now() }]);
  };

  const editBook = (id, updatedBook) => {
    setBooks(books.map((book) => (book.id === id ? { ...updatedBook, id } : book)));
  };

  const deleteBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
  };

  return { books, addBook, editBook, deleteBook };
};

export default useBooks;