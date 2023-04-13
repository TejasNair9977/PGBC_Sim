import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { 
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    LineElement,
    PointElement,
 } from 'chart.js';
import './index.scss'
 ChartJS.register(
    CategoryScale,
    LinearScale,
    LineElement,
    Title,
    Tooltip,
    Legend,
    PointElement
 );

function TrafficChart() {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Minute',
        data: [],
        borderColor: '#673ab4',
        tension: 0.1,
        fill: false,
      },
    ],
  });

  const [selectedRange, setSelectedRange] = useState(1);

  const handleButtonClick = (range) => {
    setSelectedRange(range);
  };


  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://127.0.0.1:8000/get_traffic');
      const data = await response.json();

      setChartData((prevState) => ({
        ...prevState,
        labels: [...Array(data.minute.length).keys()].map((i) => `${i}:00`),
        datasets: [
          {
            ...prevState.datasets[0],
            data: data.minute,
          },
        ],
      }));
    };

    fetchData();
  }, []);

  return (
    <div className='traffic-graph'>
      <Line data={chartData} options={{ maintainAspectRatio: false }} />
    </div>
  );
}

export default TrafficChart;
