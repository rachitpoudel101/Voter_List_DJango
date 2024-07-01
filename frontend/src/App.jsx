import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/posts`);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error("Fetching data failed:", error);
      }
    }

    fetchData();
  }, []);

  // Log data whenever it changes for debugging
  useEffect(() => {
    console.log("Data updated:", data);
  }, [data]);

  return (
    <>
      <h1>Hello World</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </>
  );
}

export default App;
