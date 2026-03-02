<!-- comentarios -->
# Proyecto: PyTest Quickstart

# Introducción
Este proyecto es una guía de inicio en PyTest en la cual aprenderas a:
- Estructurar un proyecto Python con "pyproject.toml"
- Crear funciones simples dentro de /src
- Crear tests con PyTest dentro de /test
- Generar reportes de coverage en distintos formatos (HTML, JSON, XML)
- Automatización con GitHub Actions

## Instalación
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -e .
```

## Verificamos
```bash
pytest --version
```

## Uso de funciones
```python
def dividir_seguro(a: int, b: int) -> float:
	"Divide dos numeros y lanza Valuerror si b es cero"
	if b == 0:
		raise ValueError("no se puede dividir por cero")
	return a / b
```

## Tests
```bash
pytest -v
```

## Cobertura
```bash
pytest --cov=src
```

# Automatización con GitHub Actions
