import { useEffect, useState } from "react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

function App() {
  const [ping, setPing] = useState("");

  useEffect(() => {
    fetch(`${BACKEND_URL}/ping`)
      .then((res) => res.json())
      .then((data) => setPing(data.message))
      .catch((err) => setPing("Error: Could not connect to backend"));
  }, []);

  return (
    <div>
      <h1>AadeeChat</h1>
      <p>Backend says: {ping}</p>
    </div>
  );
}

export default App;

