import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import './App.scss'
import Dashboard from './components/Dashboard';

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />}/>
        </Route>
      </Routes>
    </>
  );
}

export default App;
