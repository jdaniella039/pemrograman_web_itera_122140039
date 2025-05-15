import React, { useState } from 'react';
import AddBook from './AddBook';
import BookList from '../components/BookList';
import FilterBar from '../components/FilterBar';

const Home = () => {
  const [filter, setFilter] = useState('');

  return (
    <div>
      <h1>Daftar Buku</h1>
      <FilterBar filter={filter} setFilter={setFilter} />
      <AddBook />
      <BookList />
    </div>
  );
};

export default Home;