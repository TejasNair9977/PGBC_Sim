import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import SidebarData from './SidebarData';
import './index.scss';
import { IconButton } from '@mui/material';

const Sidebar = () => {
  return (
    <div className='Sidebar'>
      <ul className='SidebarList'>
        {SidebarData.map((val) => {
          return (
            <li key={val.id} className='navrow'>
              <NavLink activeclassname='active' activeStyle={{color:'#000000'}}>
                <Link to={val.link}>
                  <IconButton className='icon' activeClassName='active'>{val.icon}</IconButton>
                </Link>
              </NavLink>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Sidebar;
