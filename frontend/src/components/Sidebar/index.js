import React from 'react';
import { Link } from 'react-router-dom';
import SidebarData from './SidebarData';
import './index.scss';

const Sidebar = () => {
  return (
    <div className='Sidebar'>
      <ul className='SidebarList'>
        {SidebarData.map((val) => {
          return (
            <li key={val.id} className='navrow'>
              <Link to={val.link}>
                <div>{val.icon}</div>
              </Link>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Sidebar;
