import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";

const initialState = {
  labels: [],
  datasets: [
    {
      label: "Tuples Inserted",
      data: [],
      fill: false,
      backgroundColor: "#3ab466",
      borderColor: "#3ab466",
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

const TuplesInserted = () => {
  const [data, setData] = useState(initialState);

  // fetch data every second and update the graph
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://localhost:8000/tuples_inserted");
      const result = await response.json();

      const newData = {
        x: Date.now(),
        y: result.tuples_inserted,
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

export default TuplesInserted;
