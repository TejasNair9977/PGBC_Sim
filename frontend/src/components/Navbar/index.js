import React, { useState, useEffect } from 'react';
import searchpng from '../../assets/images/search.png';
import './index.scss';
import axios from 'axios';
import ViewInArIcon from '@mui/icons-material/ViewInAr';


const Navbar = () => {
  const [lastFiveBlocks, setLastFiveBlocks] = useState([]);
  const [lastEight, setLastEight] = useState('');
  const [username, setUsername] = useState('');
  const [search, setSearch] = useState('');
  const [ip ,setIp] = useState('');

  useEffect(() => {
    axios.get('/query').then((response) => {
      setLastFiveBlocks(response.data);
    });

    axios.get('/last-eight').then((response) => {
      setLastEight(response.data.last_eight);
    });

    axios.get(`http://${process.env.REACT_APP_OWN_IP}:8000/ip`).then((response) => {
      console.log(response);
      setIp(response.data.response[1])
    })
  }, []);

  return (
    <div className="nav-container">
      <form className='search-bar'>
        <input type='text' value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search..." />
        <button type='submit'>
          <img id='search' src={searchpng} alt="search icon" />
        </button>
      </form>
      <div id="blackbox">
        <ViewInArIcon style={{fontSize:'70px' , color:'#DCDCDC'}} />  {/* get */}
        <span>{ip}</span>
      </div>
    </div>
  );
};

export default Navbar;