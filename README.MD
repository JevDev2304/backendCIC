# 🚀 API de Gestión de Productos - Prueba Técnica

## 📋 Descripción

API REST para gestión de productos desarrollada con FastAPI que incluye:
- Operaciones CRUD completas
- Sincronización con API externa (Fakestore API)
- Pruebas de integración
- Documentación interactiva

## 🔧 Tecnologías Principales

- **Python 3.10+**
- **FastAPI** - Framework web
- **SQLModel** - ORM y modelos
- **MySQL** - Base de datos
- **Pytest** - Pruebas automatizadas
- **Docker** - Contenerización (opcional)

## ⚙️ Configuración

### Requisitos previos
- Python 3.10 o superior
- MySQL 8.0+
- Git

### Instalación

1. Clonar repositorio:
```bash
git clone [repo-url] && cd [repo-name]
```

2. Configurar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar el archivo .env con tus credenciales
```

## 🏃 Ejecución

Iniciar el servidor de desarrollo:
```bash
uvicorn app.main:app --reload
```

Acceder a la documentación:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📚 Endpoints

### Productos
- `GET /products` - Listar todos los productos
- `GET /products/{id}` - Obtener producto específico
- `POST /products` - Crear nuevo producto
- `PUT /products/{id}` - Actualizar producto
- `DELETE /products/{id}` - Eliminar producto
- `POST /products/sync` - Sincronizar con API externa

## 🧪 Pruebas

Ejecutar pruebas de integración:
```bash
pytest tests/
```

## 🐳 Docker (Opcional)

Construir y ejecutar con Docker:
```bash
docker-compose up --build
```

## 📌 Mejoras Futuras

1. **Autenticación y Autorización**
   - Implementar JWT con refresh tokens
   - Protección de endpoints sensibles

2. **Modelado de Datos**
   - Normalizar estructura con tabla Categorías
   - Añadir relaciones entre modelos

3. **Pruebas Automatizadas**
   - Ampliar cobertura con pruebas unitarias
   - Implementar mocks para servicios externos
   - Pruebas de rendimiento
