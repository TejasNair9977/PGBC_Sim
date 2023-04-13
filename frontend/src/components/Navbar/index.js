import React from 'react'
import { useState } from 'react'
import searchpng from '../../assets/images/search.png'
import ViewInArIcon from '@mui/icons-material/ViewInAr';
import './index.scss'

const Navbar = () => {
    const [search, setSearch] = useState("")
    

    return (
      <div className='nav-container'>
        <div className='search-bar'>
          <input type='text' value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search..." />    {/* get */}
          <img id='search' src={searchpng} alt="search icon" />
        </div>
        <div id='blackbox'>
          <div className='.icon'>
              <ViewInArIcon style={{fontSize: '30px', color:'#DCDCDC', marginRight:'3px'}} />
          </div>        
          <span>192.168.1.127</span>  {/* get */}
        </div>
      </div>
    )
}
export default Navbar
