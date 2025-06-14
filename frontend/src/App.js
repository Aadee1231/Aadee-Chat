import { useEffect, useState } from 'react';

function App() {
  const [ping, setPing] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/ping')
      .then(res => res.json())
      .then(data => setPing(data.message))
      .catch(err => setPing('Error connecting to backend'));
  }, []);

  return (
    <div>
      <h1>AadeeChat</h1>
      <p>Backend says: {ping}</p>
    </div>
  );
}

export default App;

