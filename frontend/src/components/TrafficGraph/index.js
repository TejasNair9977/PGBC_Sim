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
      backgroundColor: '#673ab4',
      borderColor: '#673ab4',
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
          beginAtZero: true,
        }
      }]
    }
  };

  useEffect(() => {
    let prevSeconds = null;
    const fetchData = async () => {
      try {
        console.log(process.env.OWN_IP)
        const response = await fetch(`http://${process.env.REACT_APP_OWN_IP}:8000/get_dynamic_traffic`);
        const data = await response.json();
        const seconds = data.response.second[0];
        const temp = data.response.second[1];
        if (prevSeconds !== null) {
          const diff = seconds - prevSeconds;
          setChartData(prevState => ({
            ...prevState,
            labels: [...prevState.labels, new Date().toLocaleTimeString()],
            datasets: [{
              ...prevState.datasets[0],
              data: [...prevState.datasets[0].data, diff]
            }]
          }));
        }
        prevSeconds = seconds;
      } catch (error) {
        console.error(error);
      }
    };
  
    const updateIntervalId = setInterval(() => {
      fetchData();
    }, 1000);
  
    const resetIntervalId = setInterval(() => {
      setChartData({
        labels: [],
        datasets: [{
          label: 'Traffic Data',
          data: [],
          backgroundColor: '#673ab4',
          borderColor: '#673ab4',
          borderWidth: 1
        }]
      });
    }, 60000);
  
    return () => {
      clearInterval(updateIntervalId);
      clearInterval(resetIntervalId);
    };
  }, []);
  

  return (
    <div className="chart-container">
      <Line className='Line' data={chartData} options={chartOptions} />
    </div>
  );
};

export default DynamicTrafficChart;
