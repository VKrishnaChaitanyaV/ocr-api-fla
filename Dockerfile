# Usa una imagen base de Python oficial (asegurándose de usar Python 3.10)
FROM python:3.10-slim

# Actualizar el sistema y instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente al contenedor
COPY . /app/

# Expone el puerto 8080
EXPOSE 8080

# Establece la variable de entorno para el puerto
ENV PORT 8080

# Define el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
