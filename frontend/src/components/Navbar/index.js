import React, { useState, useEffect } from 'react';
import searchpng from '../../assets/images/search.png';
import tejas from '../../assets/images/tejas.png';
import './index.scss';
import axios from 'axios';

const Navbar = () => {
  const [lastFiveBlocks, setLastFiveBlocks] = useState([]);
  const [lastEight, setLastEight] = useState('');
  const [username, setUsername] = useState('');

  useEffect(() => {
    axios.get('/query').then((response) => {
      setLastFiveBlocks(response.data);
    });

    axios.get('/last-eight').then((response) => {
      setLastEight(response.data.last_eight);
    });

    const storedUsername = localStorage.getItem('username');
    if (storedUsername) {
      setUsername(storedUsername);
    }
  }, []);

  return (
    <div className="nav-container">
      <form className='search-bar' onSubmit={handleSearch}>
        <input type='text' value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search..." />
        <button type='submit'>
          <img id='search' src={searchpng} alt="search icon" />
        </button>
      </form>
      <div id="blackbox">
        <img src={tejas} alt='Profile pic' />  {/* get */}
        <span>{username} #{lastEight}</span>
        <ul id="3-dot-menu">
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;