# Usa una imagen base de Python oficial
FROM python:3.10-slim

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
