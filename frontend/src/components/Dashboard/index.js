import './index.scss'
import TrafficChart from '../TrafficGraph';
import { useState } from 'react';


const Dashboard = () => {
  const [timeRange , setTimeRange] = useState('24HR');

  const handleButtonClick = (event) => {
    setTimeRange(event.target.value);
  };

  return (
    <div className='container-dashboard'>
      <div className='chart-box'>
          <div id="blackbox1">
            {/* get */}
              <span id="bbspan1">TRAFFIC</span> {/*Here will be one API endpoint*/}
          </div>

            <ul>
              <li><button value='1HR' onClick = {handleButtonClick}>1H</button></li>
              <li><button value='3HR' onClick = {handleButtonClick}>3H</button></li>
              <li><button value='12HR' onClick = {handleButtonClick}>12H</button></li>
              <li><button value='24HR' onClick = {handleButtonClick}>24H</button></li>
            </ul>
            
          <div className='graph'>
            <h2>Traffic Chart</h2>
            <TrafficChart /></div>
    </div>

    <div className='square-box timegraph'>
                  {/* get */}
        <span>SQL Query</span>
        </div>

        <div className='square-box leaderboard'>
                      {/* get */}
          <span>Leaderboard</span>
        </div>
    </div>


  )
}

export default Dashboard
