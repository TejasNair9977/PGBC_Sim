import React, { useState } from 'react';
import { NavLink, Link } from 'react-router-dom';
import SidebarData from './SidebarData';
import './index.scss';
import { IconButton } from '@mui/material';
// import MenuIcon from '@mui/icons-material/Menu';

const Sidebar = () => {

  // const [sideBar, setSideBar] = useState(false)

  // const showSideBar = () => setSideBar(!sideBar);

  return (
    <div className='Sidebar-container'>
      <div className='Sidebar'>
        {/* <Link to='#' onClick={showSideBar}>
            <IconButton>
            <MenuIcon style={{fontSize: '60px'}}/>
            </IconButton>
        </Link> */}
        {/* <nav className={sideBar ? 'nav-menu-active' : 'nav-menu'}> */}
        <ul className='SidebarList'>
          {SidebarData.map((val,key) => {
            return (
              <li key={key} className='navrow'>
                <NavLink activeclassname='active'>
                  <Link to={val.link}>
                    <IconButton className='icon' activeclassname='active'>{val.icon}</IconButton>
                  </Link>
                </NavLink>
              </li>
            );
          })}
        </ul>
        {/* </nav> */}
      </div>
    </div>
  );
};

export default Sidebar;
