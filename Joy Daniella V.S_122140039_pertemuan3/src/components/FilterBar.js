import React from 'react';

const FilterBar = ({ filter, setFilter }) => (
  <input
    type="text"
    placeholder="Cari berdasarkan judul..."
    value={filter}
    onChange={(e) => setFilter(e.target.value)}
  />
);

export default FilterBar;