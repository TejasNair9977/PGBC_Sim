import './index.scss'
import React from 'react'
import Navbar from '../Navbar'
import { Outlet } from 'react-router-dom'
import Sidebar from '../Sidebar'


const Layout = () => {
  return (
    <div className='App'>
            <Navbar />
            <Sidebar />
            <Outlet />
      </div>
  )
}

export default Layout


