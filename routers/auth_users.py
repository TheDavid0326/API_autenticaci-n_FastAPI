from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from db.models.user import User_disabled, User_password
from datetime import datetime, timedelta, timezone
import jwt
from jwt import PyJWTError

router=APIRouter(prefix="/auth",
                 tags=["auth_users"])

#Para especificar una variedad de esquemas de hash para cifrar contraseñas.
crypt=CryptContext(schemes=["bcrypt"])

#Le indicamos a FastAPI cuál es el punto de entrada específico donde se generarán los tokens de acceso "login".
#Esto es esencial para que FastAPI sepa dónde buscar la lógica de autenticación y cómo validar los tokens.
oauth2=OAuth2PasswordBearer(tokenUrl="login")

#Parámetros relacionados con el token
access_token_duration=5
algorythm="HS256"
secret="c01dfaa7ddec16fef6cef8eb9f695daf6d7d7a1bdcb8821176897bcb7b9afe8" # openssl rand -hex 32 (open ssl online)

user_list={
    "David0326": {
        "username":"David0326",
        "disabled": False,
        #"123456" con Bcrypt generator
        "password":"$2a$12$a7H.TUYTMl6WK0g1chy7EObfPDKd4Bqoxm.SXsHzYsAyp6ulNPI.u" 
    },
    "Blanky": {
        "username":"Blanky",
        "disabled": True,
        #"654321" con Bcrypt generator
        "password":"$2a$12$msxdfGuoxqd.yepbvOAvYuVvVb1X2KkqVSAkMGoMVL8BhHoIDSQeW"
    }
}

#Definimos las funciones para buscar usuarios, una devuelve solo los datos y otra devolería los datos incluyendo el password
def search_user(username:str):
    if username in user_list:
        return User_disabled(**user_list[username])

def search_user_pass(username:str):
    if username in user_list:
        return User_password(**user_list[username])

@router.post("/login")
#Con Depends() se indica a FastAPI que los datos deben enviarse como form-data, no como JSON.
#OAuth2 con OAuth2PasswordRequestForm en FastAPI requiere que los datos se envíen como form-data, no como JSON. 
# Esto se debe a que el flujo estándar de OAuth2 (y, en particular, el flujo de contraseña o password grant) 
# especifica que los datos de autenticación (usuario y contraseña) se deben enviar 
# en el cuerpo de la solicitud en formato application/x-www-form-urlencoded
async def login (form:OAuth2PasswordRequestForm=Depends()):
    #Comprobamos que el usuario existe
    user= user_list.get(form.username)
    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    #Transformamos los datos de nuestra base de datos a un objeto "found"
    found=search_user_pass(form.username)
    #Comprobamos que la contraseña es correcta
    if not crypt.verify(form.password, found.password):
        raise HTTPException (status_code=status.HTTP_401_UNAUTHORIZED, detail="La contraseña no es correcta")
    #Codificamos el token y lo retornamos
    access_token={
        "sub":form.username,
        "exp": datetime.now(timezone.utc)+timedelta(minutes=access_token_duration)
    }
    return {"access token": jwt.encode(access_token, secret, algorithm=algorythm), "token_type":"bearer"}

async def current_user(token:str=Depends(oauth2)):
    #Decodificamos el token, para encontrar el usuario
    try:
        user= jwt.decode(token, secret, algorythm)
        username= user.get("sub")#get devuelve None si no encuentra la clave
        if not username:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado en la lista de autorizados")
    except: 
        raise user.get("sub")

    user=search_user(username)
    if user.disabled==True:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Usuario desahilitado")
    return user

@router.get("/me")
async def me(user:User_disabled=Depends(current_user)):
    return user


    
