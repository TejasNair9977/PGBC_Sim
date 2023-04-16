import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";

const initialState = {
  labels: [],
  datasets: [
    {
      label: "Tuples Updated",
      data: [],
      fill: false,
      backgroundColor: "#b48e3a",
      borderColor: "#b48e3a",
    },
  ],
};

const options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    xAxes: [
      {
        type: "time",
        distribution: "series",
        time: {
          displayFormats: {
            second: "h:mm:ss a",
          },
        },
      },
    ],
  },
};

const TuplesUpdated = () => {
  const [data, setData] = useState(initialState);

  // fetch data every second and update the graph
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`http://${process.env.REACT_APP_OWN_IP}:8000/tuples_updated`);
      const result = await response.json();

      const newData = {
        x: Date.now(),
        y: result.tuples_updated,
      };

      setData((prevState) => ({
        ...prevState,
        labels: [...prevState.labels, new Date().toLocaleTimeString()],
        datasets: [
          {
            ...prevState.datasets[0],
            data: [...prevState.datasets[0].data, newData.y],
          },
        ],
      }));
    };

    const interval = setInterval(() => {
      fetchData();
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  // reset the graph every 60 seconds
  useEffect(() => {
    const resetData = () => {
      setData(initialState);
    };

    const resetInterval = setInterval(() => {
      resetData();
    }, 60000);

    return () => clearInterval(resetInterval);
  }, []);

  return <Line data={data} options={options} />;
};

export default TuplesUpdated;
