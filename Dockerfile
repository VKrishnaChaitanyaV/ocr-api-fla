FROM python:3.11-slim

# Install system dependencies required by OpenCV and EasyOCR
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgl1-mesa-glx \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port (optional, for local testing)
EXPOSE 8080

# Run the application using Waitress (for production)
CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "8080", "app:app"]
