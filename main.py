# main.py
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Inicializar la aplicación FastAPI
app = FastAPI()

# Cargar el modelo, escalador y LabelEncoder
model = joblib.load("decision_tree_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Definir el formato de entrada de datos basado en las características del dataset de Crop Recommendation
class PredictionInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

# Ruta para verificar el estado del servicio
@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente para el proyecto Crop Recommendation"}

# Ruta para realizar predicciones
@app.post("/predict/")
def predict(input_data: PredictionInput):
    # Extraer los datos de entrada y convertirlos en un formato que el modelo pueda usar
    features = np.array([[input_data.N, input_data.P, input_data.K, 
                          input_data.temperature, input_data.humidity, 
                          input_data.ph, input_data.rainfall]])

    # Aplicar el escalado de características
    features_scaled = scaler.transform(features)

    # Realizar la predicción usando el modelo
    prediction = model.predict(features_scaled)

    # Invertir la codificación de la predicción para obtener la etiqueta original
    predicted_label = label_encoder.inverse_transform(prediction.astype(int))

    # Retornar la predicción
    return {
        "predicted_crop": predicted_label[0]
    }