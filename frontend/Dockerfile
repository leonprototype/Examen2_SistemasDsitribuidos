# Utiliza una imagen oficial de Node como imagen base
FROM node:14

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo 'package.json' y 'package-lock.json' (si está disponible)
COPY package*.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia los archivos y directorios restantes al directorio de trabajo actual dentro del contenedor
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Instala el servidor HTTP para servir la aplicación React construida 
RUN npm install -g serve

# Expone el puerto que utilizará el servidor HTTP
EXPOSE 3000

# Comando para ejecutar la aplicación React con Serve
CMD ["serve", "-s", "build", "-l", "3000"]
