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


