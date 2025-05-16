# 🚀 API de Gestión de Productos - Prueba Técnica

## 📋 Descripción

API REST para gestión de productos desarrollada con FastAPI que incluye:
- Operaciones CRUD completas
- Sincronización con API externa (Fakestore API)
- Pruebas de integración
- Documentación interactiva

## 🔧 Tecnologías Principales

- **Python 3.13**
- **FastAPI** - Framework  web
- **SQLModel** - ORM y modelos
- **MySQL** - Base de datos
- **Pytest** - Pruebas automatizadas

## ⚙️ Configuración

### Requisitos previos
- Python 3.10 o superior
- MySQL 8.0+
- Git

## ⚙️ Configuración de la Base de Datos

El esquema de la base de datos MySQL se encuentra detallado en el archivo `db_schema.sql`. Este archivo incluye la creación del esquema llamado `my_app` y la tabla `products` con sus respectivas columnas y configuraciones.

## ⚙️ Configuración de la Base de Datos

El esquema de la base de datos MySQL se encuentra detallado en el archivo `db_schema.sql`. Este archivo incluye la creación del esquema llamado `my_app` y la tabla `products` con sus respectivas columnas y configuraciones.

**🛠️ Creación de la Base de Datos:**

Ejecuta el archivo `db_schema.sql` en tu terminal de MySQL o a través de MySQL Workbench. Este script creará automáticamente el esquema `my_app` y la tabla `products` con la estructura definida.

**🔗 Configuración de la Conexión:**

Una vez que hayas ejecutado el esquema, configura la conexión a la base de datos `my_app` en el archivo `.env`. Reemplaza los valores predeterminados con tu información de conexión específica. La variable `DATABASE_LINK` debe tener el siguiente formato, **asegurándote de que el nombre de la base de datos sea `my_app`**:

DATABASE_LINK=mysql+mysqlconnector://&lt;usuario>:&lt;contraseña>@&lt;host>:&lt;puerto>/my_app

Además tambien necesitas esta variable de ambiente para la URL de la api de productos externa:

EXTERNAL_API_LINK=https://fakestoreapi.com


### Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/JevDev2304/backendCIC.git
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
pytest
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
   
4. **Contenedorización con Docker**
   * Crear un Dockerfile optimizado para la aplicación
   * Configurar docker-compose para orquestar servicios (app, base de datos, etc.)
   * Implementar volúmenes para persistencia de datos
   * Definir variables de entorno para diferentes entornos (desarrollo, producción)
   * Automatizar el despliegue y pruebas en contenedores
