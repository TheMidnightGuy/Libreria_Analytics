# Stage 1: builder base
# Copiamos configuración de dependencias
# Exportamos dependencias a requirements.txt
# Descargamos dependencias en wheelhouse

FROM python:3.12.0-slim AS builder
WORKDIR /app
RUN pip install poetry poetry-plugin-export
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt
RUN pip download -r requirements.txt -d /wheelhouse

# Stage 2: imagen final autosuficiente
# Copiamos dependencias congeladas
# Instalamos offline
# Copiamos el código fuente del proyecto
# Exponer puerto para FastAPI
# Comando por defecto: arrancar FastAPI con uvicorn
FROM python:3.12.0-slim
WORKDIR /app
COPY --from=builder /wheelhouse /wheelhouse
COPY --from=builder /app/requirements.txt .
RUN pip install --no-index --find-links=/wheelhouse -r requirements.txt
COPY app/ ./app
COPY tests/ ./tests
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


