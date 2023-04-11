import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import './App.scss'
import Dashboard from './components/Dashboard';
import Login from "./components/login/Login.js"
import Register from './components/login/Register.js';
import Error from './components/Error/Error.js';

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />}/>
          <Route path ="/" element={<Login></Login>}></Route>
          {/* <Route path ="/register" element={<Register></Register>}></Route> */}
          <Route path ="/Error" element={<Error></Error>}></Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
