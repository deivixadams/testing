# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que correrá Flask
EXPOSE 5000

# Comando para iniciar la aplicación Flask
#CMD ["python", "app.py"]

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
