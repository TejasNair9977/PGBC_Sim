import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';

const TupleChart = () => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://localhost:8000/tuples_returned');
      const data = await response.json();
      const tuplesReturned = data.tuples_returned;
      const labels = [];
      const values = [];
      for (let i = 0; i < tuplesReturned.length; i++) {
        labels.push(i); // Use index as label
        values.push(tuplesReturned[i].tup_returned); // Get tup_returned as data
      }
      const chartData = {
        labels: labels,
        datasets: [
          {
            label: 'My Data',
            data: values,
            fill: false,
            backgroundColor: '#67b3a4',
            borderColor: '#67b3a4',
          },
        ],
      };
      setChartData(chartData);
    };

    fetchData(); // Fetch data once on mount

    const interval = setInterval(() => {
      fetchData(); // Fetch data every one second
    }, 1000);

    return () => clearInterval(interval); // Clear interval on unmount
  }, []);

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
};

export default TupleChart;
