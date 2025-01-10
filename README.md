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

### Aprendizajes Clave
* **FastAPI:** Profundizar en el uso de FastAPI para crear APIs RESTful de manera rápida y eficiente.
* **Autenticación** JWT: Comprender el funcionamiento de JWT para asegurar la comunicación entre cliente y servidor.
* **Hashing de contraseñas:** Utilizar Bcrypt para almacenar contraseñas de forma segura y evitar ataques de fuerza bruta.
* **Manejo de excepciones:** Utilizar excepciones HTTP para indicar errores y proporcionar respuestas significativas al cliente.
* **Validación de datos:** Implementar validación de datos para garantizar la integridad de los datos ingresados por el usuario.
* **Diseño de APIs:** Diseñar APIs RESTful siguiendo buenas prácticas y estándares.
* **Seguridad:** Comprender los conceptos básicos de seguridad en APIs, como la protección contra ataques de inyección y la importancia de almacenar las claves de forma segura.
* **MongoDB:** Interactuar con una base de datos NoSQL como MongoDB para almacenar y recuperar datos de usuarios.

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
