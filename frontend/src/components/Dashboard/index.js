import './index.scss'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Dashboard = () => {
  return (
    <div className='container-dashboard'>
      <div className='chart-box'>
          <div id="blackbox1">
            {/* get */}
              <span id="bbspan1">TRAFFIC</span> {/*Here will be one API endpoint*/}
          </div>

            <ul>
              <li>1H</li>
              <li>3H</li>
              <li>12H</li>
              <li>24H</li>
            </ul>

          <div className='graph'>{/*Graph goes here*/}</div>
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
