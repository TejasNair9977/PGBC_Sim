import React from 'react'
import { useState } from 'react'
import searchpng from '../../assets/images/search.png'
import tejas from '../../assets/images/tejas.png'
import './index.scss'

const Navbar = () => {
    const [search, setSearch] = useState("")
    

    return (
      <div className='nav-container'>
          <input type='text' value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search..." />             {/* get */}
          <img id='search' src={searchpng} alt="search icon" />
        <div id='blackbox'>
          <img src={tejas} alt='Profile pic' />             {/* get */}
          <span>Tejas Nair</span>                           {/* get */}
          <ul id='3-dot-menu'>
            <li></li>
            <li></li>
            <li></li>
          </ul>
        </div>
      </div>
    )
}
export default Navbar
