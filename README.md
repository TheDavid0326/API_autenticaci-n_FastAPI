## API de Autenticación de Usuarios en FastAPI

### Descripción
Esta API proporciona endpoints para gestionar usuarios, incluyendo registro, inicio de sesión, actualización y eliminación. Utiliza FastAPI, una framework de Python para crear APIs modernas, y JWT para autenticación.

### Funcionalidades
* **Registro de usuarios:** Permite crear nuevos usuarios con nombre de usuario y contraseña.
* **Inicio de sesión:** Autentica a los usuarios y genera un token de acceso JWT.
* **Obtener información del usuario actual:** Permite obtener información del usuario actualmente autenticado.
* **Actualizar información del usuario:** Permite actualizar la información de un usuario existente.
* **Eliminar un usuario:** Permite eliminar un usuario.

### Tecnologías utilizadas
* **FastAPI:** Framework de Python para crear APIs.
* **Python:** Lenguaje de programación principal.
* **JWT:** JSON Web Tokens para autenticación.
* **Bcrypt:** Para el hash de contraseñas.
* **MongoDB** (implicito): Se asume que se utiliza MongoDB como base de datos.

### Estructura de la API
* **Rutas de usuarios:** `/userdb`
* **Rutas de autenticación:** `/auth`

### Cómo utilizar la API
1. **Iniciar el servidor FastAPI:** Ejecutar el comando `uvicorn users_db:app --reload` en la terminal.
2. **Realizar solicitudes HTTP:** Utilizar herramientas como Postman o curl para enviar solicitudes a los endpoints de la API.

### Ejemplos de solicitudes
* **POST /userdb**
Cuerpo de la solicitud (JSON):
{
    "username": "nuevo_usuario",
    "password": "contraseña_segura"
}

* **Inicio de sesión(POST /auth/login):**
Cuerpo de la solicitud (form-data):

username=nuevo_usuario
password=contraseña_segura

### Consideraciones importantes(Seguridad)
* **Hashing de contraseñas:** Se utiliza Bcrypt para almacenar las contraseñas de forma segura.
* **JWT:** Los tokens JWT se utilizan para autenticar a los usuarios y deben ser almacenados de forma segura.
* **Validación:** Se realiza una validación básica de los datos de entrada para prevenir ataques de inyección.
* **Manejo de errores:** Se utilizan excepciones HTTP para indicar diferentes tipos de errores.
