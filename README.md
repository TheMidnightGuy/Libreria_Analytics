# Libreria Analytics

## Índice
* [¿Qué es?](#qué-es)
* [Instalación](#instalación)
* [Como usar](#cómo-usar)
* [Crear template](#crear-un-template)
* [Obtener template](#obtener-un-template)
* [Flujo de selección y generación](#flujo-de-selección-y-generación)

## ¿Qué es?
Un ecosistema centralizado de archivos diseñado para estandarizar el desarrollo de proyectos. Encapsula estructuras reutilizables permitiendo que cualquier usuario pueda utilizarlo como base solida y probada.

## Propósito
El objetivo principal de este repositorio es acceder a templates de archivos y/o proyectos de manera sencilla.
Mediante el uso de la herramienta **Copier** este repositorio permite:

- **Estandarización:** Garantiza que todos los proyectos se guíen bajo un estándar definido.
- **Agilidad:** Desplegar un entorno de trabajo completo en cuestión de segundos mediante sencillos comandos.
- **Mantenibilidad:** Facilitar la actualización de proyectos cuando los estándares se modernizan.

# Instalación

### Prerrequisitos

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
		├── 📁 fastapi                  # Carpeta con nombre configurable para template
		│   ├──  "copier.yaml"          # Archivo de configuración Copier
		│   ├──  app.py                 # Archivos del proyecto
		│   ├──  pyproject.toml
		│   ├──  Dockerfile   
		│   └──  .gitignore                  	

```

# ¿Cómo usar?

Contamos con dos formas de uso principales
- Crear un template
- Obtener un template

A continuación veremos el paso a paso de cada uno.

## Crear un template
Antes de empezar necesitamos del archivo `copier.yml`, este será nuestro
archivo de configuración a la hora de crear un template.

Todo lo que este en la misma ruta que este archivo será utilizado para crear un template

```yaml
#copier.yml - main
#Copier configuración
min_copier_version: "9.11.0"

#Formato: tipo + nombre_template
#Tipo: project, analytics, tool
instrucciones:
  type: str
  help: "
  
    ------------------------------------------------------
    LIBRERIA DE ANALYTICS

    Formato de selección:
    * project-  : Estructura completa de un proyecto
    * analytics : Dashboards y herramientas de analisis
    * tool      : Archivos individuales o utilidades

    (ej: project-pytest / analytics-grafana / tool-docker)

    Presiona ENTER para continuar...
    ------------------------------------------------------"
  default: ok

#Listado de templates disponible en repositorio.
#Preguntamos al usuario que plantilla desea obtener
selected_template:
  type: str
  help: "Ingresar nombre de template que desea generar ¡Recordar prefijos antes del nombre del template!"
  validator: "{{'¡Ingresar nombre valido!' if not selected_template }}"

#subdirectory -> Se obtiene la variable para dirigirse al template correcto. 
_subdirectory: "templates/{{selected_template}}"

#Se crea un archivo que guarda todas las respuestas cuando el template fue creado.
#Este es necesario para en el futuro usar "> copier update".
_answers_file: .mycustom-answers.yml

```

## Obtener un template
Tenemos distintas maneras de obtener templates pero ambas siguen la misma lógica

Podemos generar un proyecto a partir de un template mediante la herramienta CLI `copier`
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
Al ejecutar el comando principal `copier copy` para obtener un template, entraras en un asistente dentro de la consola de tipo pregunta respuesta. **Copier** se encargara de redirigir la instalación al subdirectorio correcto.

A continuación se detalla el paso a paso a seguir.

1. Comando de generación

Ejecuta el comando en la terminal:
```powershell
copier copy gh:TheMidnightGuy/Libreria_Analytics .
```

2. Convención de nombres
```powershell
    ------------------------------------------------------
    LIBRERIA DE ANALYTICS

    Formato de selección:
    * project-  : Estructura completa de un proyecto
    * analytics- : Dashboards y herramientas de analisis
    * tools-      : Archivos individuales o utilidades

    (ej: project-pytest / analytics-grafana / tools-docker)

    Presiona ENTER para continuar...
    ------------------------------------------------------"
```

3. Interfaz de selección

Usuario debe ingresar en texto el nombre del template que necesita
```powershell
🎤 Escribe el nombre del template que desea usar
   project-fastapi
```

4. Confirmación de creación

Tras responder correctamente se vera el resumen de los archivos generados y el template se habra generado correctamente
```powershell
Copying from project-python_app version 1.0.0
    create  app.py
    create  pyproject.toml
    create  Dockerfile
    create  .copier-answers.yml
```

# Convención de nombres

Para facilitar la búsqueda y mantenimiento, todos los templates siguen una nomenclatura basadas en prefijos:
- `project-`: Templates de proyectos completos (Archivos base, estructuras de carpetas, CI/CD...)
- `analytics-`: Dashboards y herramientas de análisis de datos
- `tools-`: Archivos individuales o utilidades

 Esta estructura permite añadir nuevos templates de manera sencilla bajo un prefijo que la identifica.

**Atención:** Aquellos nombres de templates que se ingresen sin prefijo terminaran en error al intentar generar un template
