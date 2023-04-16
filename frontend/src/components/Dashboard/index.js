import './index.scss'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DynamicTrafficChart from '../TrafficGraph';

const Dashboard = () => {
  const [peers, setPeers] = useState([]); // Leaderboard
  const [lastFiveBlocks, setLastFiveBlocks] = useState([]); //Queries

  useEffect(() => {
    axios.get(`http://${process.env.REACT_APP_OWN_IP}:8000/get_peers`).then((response) => {
      setPeers(response.data.response.peers)

    });

    axios.get(`http://${process.env.REACT_APP_OWN_IP}:8000/query`).then((response) => {
      setLastFiveBlocks(response.data.response);
    });
  }, []);

  return (
    <div className='container-dashboard'>
      <div className='chart-box'>
        <div id="blackbox1">
          <span id="bbspan1">TRAFFIC</span>
        </div>
        <ul>
          <li>1H</li>
          <li>3H</li>
          <li>12H</li>
          <li>24H</li>
        </ul>
        <div className='graph'><DynamicTrafficChart /></div>
      </div>

      <div className='square-box timegraph'>
        <span>SQL Query</span>
        <ul>
        {lastFiveBlocks.map((query, index) => (
           <li key={index}>{query.message} <br/> {query.timestamp}</li>
          ))}
        </ul>
      </div>

      <div className='square-box leaderboard'>
        <span>Leaderboard</span>
        <ul>
          {peers.map((peer, index) => (
            <li key={index}>{peer}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;

