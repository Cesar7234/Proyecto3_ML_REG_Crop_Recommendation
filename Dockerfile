# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y el código fuente
COPY requirements.txt requirements.txt
COPY . .

# Copiar el archivo del modelo al contenedor
COPY decision_tree_model.pkl /app/decision_tree_model.pkl

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
