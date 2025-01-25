from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Load trained model
MODEL_PATH = "models/model.pkl"

class PredictionRequest(BaseModel):
    features: list

@app.on_event("startup")
async def load_model():
    """Load the trained model when the API starts"""
    try:
        global model
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error loading model: {str(e)}"
        )

@app.post("/predict")
async def predict(request: PredictionRequest):
    """Make predictions using the trained model"""
    try:
        prediction = model.predict([request.features])
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction error: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv('API_HOST', '0.0.0.0'),
        port=int(os.getenv('API_PORT', 8000))
    )
