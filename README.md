# Libreria Analytics

## Índice
* [¿Qué es?](#qué-es)
* [Instalación](#instalación)
* [Como usar](#como-usar)
* [Crear plantilla](#crear-una-plantilla)
* [Obtener plantilla](#obtener-una-plantilla)
* [Flujo de selección y generación](#flujo-de-selección-y-generación)

## ¿Qué es?
Un ecosistema centralizado de archivos diseñado para estandarizar el desarrollo de proyectos. Encapsula estructuras reutilizables permitiendo que cualquier usuario pueda utilizarlo como base solida y probada.

## Proposito
El objetivo principal de este repositorio es acceder a plantillas de archivos y/o proyectos de manera sencilla.
Mediante el uso de la herramienta **Copier** este repositorio permite:

- **Estandarización:** Garantiza que todos los proyectos se guien bajo un estandar definido.
- **Agilidad:** Desplegar un entorno de trabajo completo en cuestión de segundos mediante sencillos comandos.
- **Mantenibilidad:** Facilitar la actualización de proyectos cuando los estandares se modernizan.

# Instalación

### Prerequisitos

Se requiere tener instalado ciertos componentes previo instalación de **Copier**.

- Python en versión 3.10 o superior
- Git en versión 2.27 o superior
- Poetry en versión 2.3.2 o superior

**Tipos de instalación**

- CLI (Command Line Interface):  `pipx install copier` o `uv tool install copier`
- Libreria: `pip install copier` o `conda install -c conda-forge copier`

# Estructura de carpetas
```powershell
Estructura de carpetas estandar

		📁 Templates                    # Nombre de mi proyecto original
		├── 📁 fastapi                  # Carpeta con nombre configurable para plantilla
		│   ├──  "copier.yaml"          # Archivo de configuración Copier
		│   ├──  app.py                 # Archivos del proyecto
		│   ├──  pyproject.toml
		│   ├──  Dockerfile   
		│   └──  .gitignore                  	

```

# ¿Como usar?

Contamos con dos formas de uso principales
- Crear una plantilla
- Obtener un template

A continuación veremos el paso a paso de cada uno.

## Crear una plantilla
Antes de empezar necesitamos del archivo `copier.yml`, este sera nuestro
archivo de configuración a la hora de crear una plantilla.

Todo lo que este en la misma ruta que este archivo sera utilizado para crear una plantilla

```yaml
#copier.yml
#Copier configuración
min_copier_version: "9.11.0"

#Se listan los templates disponibles
#y preguntamos al usuario que plantilla desea obtener
selected_template:
  type: str
  help: "Selecciona la plantilla que deseas usar:"
  choices:
    - fastapi
    - pytest

#subdirectory -> Se obtiene la variable para dirigirse a la plantilla correcta.
# Se dirige a la ruta dentro del proyecto.
_subdirectory: "templates/{{selected_template}}"

#Pregunto si instalo dependencias dentro del templete
dependencies_install:
    type: bool
    help: "¿Instalar dependencias?"
    default: true

#Instalo las dependencias desde poetry
_task:
 - command: ["poetry", "install"]
   when: dependencies_install

#Se crea un archivo que guarda todas las respuestas cuando el template fue creado.
#Este es necesario para en el futuro usar "copier update".
_answers_file: .mycustom-answers.yml

```

## Obtener una plantilla
Tenemos distintas maneras de obtener plantillas pero ambas siguen la misma lógica

Podemos generar un proyecto a partir de una plantilla mediante la herramienta CLI `copier`
```powershell
copier copy ruta/de/origen ruta/de/destino
```

Esto funciona tanto en local como repositorios en GitHub.
Ejemplos
- Local:
```powershell
copier copy "../proyectos/mi_plantilla_copier" .
``` 
- GitHub: 
```powershell
copier copy "https://github.com/TheMidnightGuy/Libreria_Analytics.git" .
```
```powershell
copier copy gh:TheMidnightGuy/Libreria_Analytics .
```

---

# Flujo de selección y generación
Al ejecutar el comando principal `copier copy` para obtener una plantilla, entraras en un asistente dentro de la consola de tipo pregunta respuesta. **Copier** se encargara de redigirir la instalación al subdirectorio correcto.

A continuación se detalla el paso a paso a seguir.

1. Comando de generación

Ejecuta el comando en la terminal:
```powershell
copier copy gh:TheMidnightGuy/Libreria_Analytics .
```

2. Interfaz de selección interactiva

Veras un menú donde podras navegar con las flechas del teclado (`↑` `↓`) y confirmar con `Enter`.
```powershell
🎤 Selecciona la plantilla que deseas usar:
❯ projects          # Redirige a templates/projects
  analytics        # Redirige a templates/analytics
  tools            # Redirige a templates/tools (archivos individuales)
```

3. Confirmación de creación

Tras responder correctamente se vera el resumen de los archivos generados y la plantilla se habra generado correctamente
```powershell
Copying from template version 1.0.0
    create  app.py
    create  pyproject.toml
    create  Dockerfile
    create  .copier-answers.yml
```
