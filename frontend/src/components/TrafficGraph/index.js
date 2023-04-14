import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { 
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    Title,
    Tooltip,
    Legend,
    LineElement,
    PointElement,
 } from 'chart.js';
import './index.scss';

ChartJS.register(
    CategoryScale,
    LinearScale,
    LineElement,
    Title,
    Tooltip,
    Legend,
    PointElement
);

const DynamicTrafficChart = () => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [{
      label: 'Traffic Data',
      data: [],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  });

  const chartOptions = {
    scales: {
      xAxes: [{
        type: 'realtime',
        realtime: {
          delay: 1000,
          pause: false,
          onRefresh: function(chart) {
            chart.data.datasets.forEach(function(dataset) {
              dataset.data.push({
                x: Date.now(),
                y: dataset.lastValue
              });
            });
          }
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/get_dynamic_traffic');
        const data = await response.json();
        setChartData(prevState => ({
          ...prevState,
          labels: [...prevState.labels, new Date().toLocaleTimeString()],
          datasets: [{
            ...prevState.datasets[0],
            data: [...prevState.datasets[0].data, data.response.second]
          }]
        }));
      } catch (error) {
        console.error(error);
      }
    };

    const intervalId = setInterval(() => {
      fetchData();
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div className="chart-container">
      <Line className='Line' data={chartData} options={chartOptions} />
    </div>
  );
};

export default DynamicTrafficChart;
