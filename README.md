# Crop Production Prediction Project

Este proyecto utiliza un modelo de regresión para predecir el tipo de cultivo adecuado según las condiciones de entrada proporcionadas. El modelo ha sido entrenado utilizando datos de producción agrícola, y la API desarrollada con FastAPI permite realizar predicciones basadas en nuevos datos.

## Estructura del Proyecto

- `model_training.py`: Script para entrenar el modelo `DecisionTreeRegressor` y guardarlo en formato `.pkl` utilizando joblib.
- `model_inference.py`: Script para cargar el modelo entrenado, hacer predicciones sobre nuevos datos y evaluar el rendimiento.
- `app.py`: Implementación de una API con FastAPI para realizar predicciones en tiempo real.
- `preprocessed_data.pkl`: Archivo con los datos ya preprocesados (separados en train y test).
- `decision_tree_model.pkl`: Modelo entrenado serializado.
- `scaler.pkl`: Scaler serializado para normalizar los datos.
- `label_encoder.pkl`: Codificador de etiquetas serializado para las predicciones.
  
## Requisitos

Las siguientes bibliotecas son necesarias para ejecutar el proyecto. Estas se encuentran listadas en el archivo `requirements.txt`.

## Instalación y Ejecución

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/crop-prediction.git
   cd crop-prediction

2. Crear un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instalar las dependencias:
pip install -r requirements.txt

4.Entrenar el modelo (si deseas volver a entrenarlo):
python model_training.py

5. Ejecutar la API de FastAPI:
uvicorn app:app --reload
La API estará disponible en http://127.0.0.1:8000.

7. Probar la API: Puedes hacer una solicitud POST para obtener predicciones utilizando herramientas como curl o Postman:
curl -X 'POST' \
'http://127.0.0.1:8000/predict' \
-H 'Content-Type: application/json' \
-d '{
"N": 100,
"P": 40,
"K": 50,
"temperature": 25.5,
"humidity": 60.2,
"ph": 6.5,
"rainfall": 120.0
}'
La respuesta debería ser el nombre del cultivo más adecuado.

Contribución
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Crea un fork del repositorio.
2. Crea una rama con el nombre de la característica que agregarás (git checkout -b feature/nueva-caracteristica).
3. Haz commit de tus cambios (git commit -am 'Agrego nueva característica').
4. Haz push de la rama (git push origin feature/nueva-caracteristica).
5. Crea un nuevo Pull Request.

Licencia
Este proyecto está bajo la licencia MIT.