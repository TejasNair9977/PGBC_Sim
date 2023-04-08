import './index.scss'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Dashboard = () => {
  return (
    <div className='container-dashboard'>
      <div className='chart-box'>
          <div id="blackbox1">
              <span id="bbspan1">SQL QUERY</span> {/*Here will be one API endpoint*/}
          </div>

          <ul>
            <li>1H</li>
            <li>1W</li>
            <li>1M</li>
            <li>3M</li>
          </ul>
    </div>

    <div className='square-box timegraph'>
        <span>Time Date</span>
        </div>

        <div className='square-box leaderboard'>
          <span>leaderboard</span>
        </div>
    </div>


  )
}

export default Dashboard
