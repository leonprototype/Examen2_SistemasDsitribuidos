# Usar una imagen oficial de Python como imagen padre
FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Hacer que el puerto 5000 esté disponible para el mundo exterior
EXPOSE 5000

# Ejecutar app.py cuando el contenedor se inicie
CMD ["flask", "run", "--host=0.0.0.0"]