### FastAPI User Administration REST API

Esta es una aplicación básica de API REST creada con FastAPI para administrar usuarios y sus direcciones. La API proporciona endpoints para crear, obtener, actualizar y eliminar usuarios, así como para obtener usuarios por país en sus direcciones.

### Configuración y Ejecución

1. **Configuración del Entorno Virtual**

   Antes de ejecutar la aplicación, asegúrate de activar tu entorno virtual (venv). Puedes hacerlo ejecutando el siguiente comando en tu terminal o símbolo del sistema:

   - En Windows:

     ```
     venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```
     source venv/bin/activate
     ```

2. **Instalación de Dependencias**

   Asegúrate de tener Python y pip instalados. Luego, instala las dependencias ejecutando:

   ```
   pip install fastapi uvicorn sqlalchemy
   ```

3. **Base de Datos**

   Asegúrate de tener una base de datos configurada. Este código asume el uso de SQLAlchemy con una estructura de base de datos ya definida. Asegúrate de configurar las credenciales de la base de datos en `config/database.py`.

4. **Ejecución de la Aplicación**

   Ejecuta la aplicación utilizando el siguiente comando:

   ```
   uvicorn main:app --reload
   ```

   Esto iniciará el servidor FastAPI y la API estará disponible en `http://localhost:8000`.

### Endpoints de la API

- **`POST /users`**
  - Crear un nuevo usuario con dirección.
  - Parámetros de entrada: nombre, apellido, edad, correo electrónico, contraseña y dirección.
  
- **`GET /users`**
  - Obtener todos los usuarios con sus direcciones.
  
- **`GET /users/{id}`**
  - Obtener un usuario por su ID con su dirección.
  
- **`PUT /users/{id}`**
  - Actualizar un usuario existente y su dirección.
  - Parámetros de entrada: nombre, apellido, edad, correo electrónico, contraseña y dirección.
  
- **`DELETE /users/{id}`**
  - Eliminar un usuario por su ID con su dirección.
  
- **`GET /users/country/{country}`**
  - Obtener usuarios por el nombre de su país en la dirección.

### Modelo de Datos

- **Usuario (`UserModel`)**: 
  - ID (Generado automáticamente)
  - Nombre
  - Apellido
  - Edad
  - Correo Electrónico
  - Contraseña
  - Dirección (`AddressModel`)
  
- **Dirección (`AddressModel`)**: 
  - ID (Generado automáticamente)
  - Dirección 1
  - Dirección 2
  - Ciudad
  - Estado
  - Código Postal
  - País

### Notas Importantes

- Las solicitudes y las respuestas se manejan en formato JSON.
- La aplicación maneja errores, incluyendo casos de usuario no encontrado.
- Se han proporcionado endpoints para todas las operaciones especificadas en el desafío.

Recuerda modificar las configuraciones de la base de datos y otros detalles específicos de tu implementación antes de ejecutar la aplicación. ¡Buena suerte con tu desafío!# api-user-python
