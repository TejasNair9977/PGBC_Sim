import './index.scss'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DynamicTrafficChart from '../TrafficGraph';

const Dashboard = () => {
  const [peers, setPeers] = useState([]); // Leaderboard
  const [lastFiveBlocks, setLastFiveBlocks] = useState([]); //Queries

  useEffect(() => {
    axios.get('/get_peers').then((response) => {
      setPeers(response.data);
    });

    axios.get('/query').then((response) => {
      setLastFiveBlocks(response.data);
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
        <ol>
          {lastFiveBlocks.map((block, index) => (
            <li key={index}>{block}</li>
          ))}
        </ol>
      </div>

      <div className='square-box leaderboard'>
        <span>Leaderboard</span>
        <ol>
          {peers.map((peer, index) => (
            <li key={index}>{peer}</li>
          ))}
        </ol>
      </div>
    </div>
  );
};

export default Dashboard;

