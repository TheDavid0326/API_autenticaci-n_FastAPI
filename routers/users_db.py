from fastapi import APIRouter, status, HTTPException
from bson import ObjectId
from db.client import db_client
from db.models.user import User
from db.schemas.user import user_schema, users_schema

# con "responses" puedes especificar de manera precisa qué tipo de respuesta se espera para cada código de estado HTTP.
router=APIRouter(prefix="/userdb",
                 tags=["userdb"],
                 responses={
                     404:{"description":"No hay nada aquí"},
                     200:{"description":"Se ha procesado todo bien"}
                    }
                )

#cd 1.-Python/Ejercicios/FastAPI/routers
#uvicorn users_db:app --reload

@router.get("/")
async def users():
    return users_schema(db_client.userdb.find())

@router.post("/", response_model=User)
async def user_post(user:User):
    #Comprobar que el correo no exista ya
    Found=search_user("email",user.email)
    if type(Found)==User:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail="El email ya está registrado, usa otro email")
    #Transformarlos al formato de la base de datos
    dict_user=dict(user)
    del dict_user["id"]
    #Meterlos a la base de datos y quedarnos con el nuevo ID
    new_id=db_client.userdb.insert_one(dict_user).inserted_id
    #Verificar y mostrar el resultado del nuevo usuario introducido
    return search_user("_id",new_id)

def search_user(field:str,key):
    try:
        user=user_schema(db_client.userdb.find_one({field:key}))
        return User(**user)
    except:
        return {"Error":"El usuario no existe"}

#Actualizar todo el usuario completo
@router.put("/", status_code=status.HTTP_202_ACCEPTED,response_model=User )
async def update_user(user:User):
    #Comprobar que el id exista
    Found=search_user("_id",ObjectId(user.id))
    if type(Found)!=User:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail="No existe ningún usuario con ese id")
    #Transformar los nuevos datos al formato de la base de datos
    dict_user=dict(user)
    del dict_user["id"]
    #Meterlos a la base de datos reemplazando los anteriores
    db_client.userdb.find_one_and_replace({"_id":ObjectId(user.id)},dict_user)
    #Verificar y mostrar el resultado de los nuevos datos actualizados
    return search_user("_id",ObjectId(user.id))

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED )
async def delete_user(id:str):
    #Comprobar que el id exista
    Found=search_user("_id",ObjectId(id))
    if type(Found)!=User:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail="No existe ningún usuario con ese id, no se puede eliminar")
    #Eliminarlo de la base de tatos
    db_client.userdb.find_one_and_delete({"_id":ObjectId(id)})
    #Verificar y mostrar el resultado de los nuevos datos actualizados
    return {"detail":f"El usuario con el id:{id} ha sido eliminado"}


