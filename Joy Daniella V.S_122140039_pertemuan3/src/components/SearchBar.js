import React from 'react';

const SearchBar = ({ query, setQuery }) => (
  <input
    type="text"
    placeholder="Cari buku..."
    value={query}
    onChange={(e) => setQuery(e.target.value)}
  />
);

export default SearchBar;