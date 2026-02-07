# CARDIO-GUARD

AI-powered Heart Disease Risk Prediction System
CARDIO-GUARD 
An interpretable machine learning dashboard for early cardiovascular disease risk prediction using real biomedical data. This project uses a FastAPI backend to serve a Machine Learning model and a React frontend for a modern, interactive user experience.

Project Structure
Plaintext
CARDIO-GUARD/
├── backend/            # FastAPI Server & ML Model
│   ├── main.py         # API endpoints
│   └── model.joblib    # Trained ML Model
├── frontend/           # React App (Tailwind CSS)
│   ├── src/
│   │   └── App.js      # Main Dashboard Logic
│   └── package.json
├── heart_processed.ipynb # Model Training Notebook
└── heart_processed.csv   # Dataset
