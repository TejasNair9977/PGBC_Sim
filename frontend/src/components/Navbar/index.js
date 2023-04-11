import React, { useState, useEffect } from 'react';
import searchpng from '../../assets/images/search.png';
import tejas from '../../assets/images/tejas.png';
import './index.scss';
import axios from 'axios';

const Navbar = () => {
  const [search, setSearch] = useState('');
  const [lastFiveBlocks, setLastFiveBlocks] = useState([]);
  const [lastEight, setLastEight] = useState('');

  useEffect(() => {
    axios.get('/query').then((response) => {
      setLastFiveBlocks(response.data);
    });

    axios.get('/last-eight').then((response) => {
      setLastEight(response.data.last_eight);
    });
  }, []);

  return (
    <div className="nav-container">
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search..." 
      /> {/* get */}
      <img id="search" src={searchpng} alt="search icon" />
      <div id="blackbox">
        <img src={tejas} alt='Profile pic' />  {/* get */}           
        <span>Tejas Nair {lastEight}</span> {/* get */}
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

