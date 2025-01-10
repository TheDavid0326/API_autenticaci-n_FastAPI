from fastapi import FastAPI
from routers import users_db, auth_users

app=FastAPI()

#cd 1.-Python/Ejercicios/FastAPI
#uvicorn main:app --reload

#routers


app.include_router(users_db.router)
app.include_router(auth_users.router)






