#Realizar un API Rest para almacenar la informacion de las canciones que maneja spotify. Los datos requeridos minimos 
# son: Nombre de la cancion, descripcion, artista, duracion en segundos, 
# extension de la cancion, album, año.
#Los HTTP a implementar
#POST
#GET. Desplegar todas la canciones asi como por nombre de la cancion.
#PUT
#DELETE.
#En total son 5 recursos.

from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app = FastAPI()

class Canciones (BaseModel):
    id:int 
    name:str
    description:str
    artist:str
    duration:int
    extension:str
    album:str
    anio:int

    class Config:
        orm_mode=True

db = SessionLocal()
@app.get('/canciones',response_model=List[Canciones],status_code=200)
def get_all_items():
    canciones = db.query(models.Canciones).all()
    return canciones #retorno de toda la lista.

@app.get('/canciones/{canciones_id}',response_model=Canciones,status_code=status.HTTP_200_OK)
def get_an_item(canciones_id:int):
    canciones=db.query(models.Canciones).filter(models.Canciones.id ==canciones_id).first()
    return canciones

@app.post('/cancion',response_model=Canciones,
        status_code=status.HTTP_201_CREATED)
def create_an_item(canciones:Canciones):
    db_Canciones=db.query(models.Canciones).filter(models.Canciones.name==canciones.name).first()

    if db_Canciones is not None:
        raise HTTPException(status_code=400,detail="Cancion ya existe")    

    new_cancion=models.Canciones(
        name=canciones.name,
        description=canciones.description,
        artist=canciones.artist,
        duration=canciones.duration,
        extension=canciones.extension,
        album=canciones.album,
        anio=canciones.anio
    )
    db.add(new_cancion)
    db.commit()

    return new_cancion

@app.put('/canciones/{canciones_id}',response_model=Canciones,status_code=status.HTTP_200_OK)
def update_an_item(canciones_id:int,canciones:Canciones):
    canciones_to_update=db.query(models.Canciones).filter(models.Canciones.id==canciones_id).first()
    canciones_to_update.name=canciones.name
    canciones_to_update.description=canciones.description
    canciones_to_update.artist=canciones.artist
    canciones_to_update.duration=canciones.duration
    canciones_to_update.extension=canciones.extension
    canciones_to_update.album=canciones.album
    canciones_to_update.anio=canciones.anio


    db.commit()

    return canciones_to_update

@app.delete('/canciones/{canciones_id}')
def delete_item(canciones_id:int):
    canciones_to_delete=db.query(models.Canciones).filter(models.Canciones.id==canciones_id).first()

    if canciones_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    db.delete(canciones_to_delete)
    db.commit()

    return canciones_to_delete
