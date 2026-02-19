#Template Dockerfile.
#Autor: BENJAMIN.P

#Dockerfile ¿Qué es?
#Es un archivo de texto en el cual se definen instrucciones de manera estructurada y secuencial para crear una imagen Docker.

#El archivo "Dockerfile" esta compuesto por:
# FROM:     Aqui se define la imagen base que usaremos junto con su versión y variante (slim/alpine/standard) (ej.- python:3.12-slim)
# WORKDIR:  Define el directorio de trabajo o raiz base del proyecto.
# COPY:     Copia los archivos del proyecto hacia la imagen Docker que se esta creando.
# RUN:      Ejecuta comandos en consola (CLI) una vez (EJ.- instalación de dependencias.)
# CMD:      Son los comandos que se ejecutan al final una vez ya esta ejecutado el servicio al iniciar un contenedor.

#Buenas prácticas:
# Multi-Stage: Se basa en estructurar por partes el archivo docker, dedicando objetivos en especifico a cada una de estas.
# Almacenamiento en caché: Es un conjunto de buenas prácticas que permiten optimizar el proceso de creación de imagenes cuando se crea un contenedor.
# Tags: Existen distintos tipos de tags los cuales estan principalmente orientados a la identificación de versiones y/o apodos a imagenes Docker.

#Dependiendo del objetivo de la app y como este construida puede variar el uso de ciertos comandos.

#Ejemplo 1. Python app simple
#Dockerfile
#Imagen base para build de imagen.
#Se trabaja en el directorio 'src'
#Se copia la app a la imagen docker
#Se ejecutan los comandos (CLI) para que se inicie la app
FROM python:3.12.0-slim
WORKDIR /src
COPY app.py .
CMD ["python", "app.py"]

#Buenas prácticas
#1. Almacenamiento en cache
#Esta compuesto por distintas prácticas las cuales veremos en conjunto en un ejemplo
FROM python:3:12.0-slim
WORKDIR /app
RUN --mount=type=bind,target= "comando de build de imagen Docker"
RUN --mount=type=cache,target=root pip install -r requirements.txt
CMD ["python", "app.py"]

#Tras este ejemplo podemos ver que cumple con:
#1. Una estructura logica secuencial ahorrando cache
#2. Uso de 'bind mounts', para sincronizar cambios en tiempo real en la imagen si se reconstruye por ejemplo
#3. Uso de 'cache mounts', para persistir directorios de paquetes entre construcciones de imagen. Evitando descargas nuevas en cada ejecución



