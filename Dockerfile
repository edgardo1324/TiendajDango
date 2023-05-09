# Define la imagen base de Docker
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el proyecto Django al contenedor
COPY . .

# Expone el puerto 8000 para acceder a la aplicación web
EXPOSE 8000

# Ejecuta el comando para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

