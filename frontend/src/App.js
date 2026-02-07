import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    age: 50, sex: 1, cp: 0, trestbps: 120, chol: 200,
    fbs: 0, restecg: 0, thalach: 150, exang: 0,
    oldpeak: 1.0, slope: 1, ca: 0, thal: 2
  });
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:8000/predict', formData);
    setResult(res.data);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-center text-red-600 mb-8">
        CARDIO-GUARD Dashboard
      </h1>
    </div>
  );
}

export default App;
