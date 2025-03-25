from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List
import os

# Definir el camí al fitxer JSON
FITXER_ALUMNES = "alumnes.json"

# Crear el model de dades per l'alumne
class Alumne(BaseModel):
    id: int
    nom: str
    cognom: str
    dia_naixement: int
    mes_naixement: int
    any_naixement: int
    email: str
    feina: bool
    curs: str

# Crear la instància de FastAPI
app = FastAPI()

# Funció per llegir dades del fitxer JSON
def llegir_dades():
    if not os.path.exists(FITXER_ALUMNES):
        return []
    with open(FITXER_ALUMNES, "r") as f:
        return json.load(f)

# Funció per escriure dades al fitxer JSON
def escriure_dades(alumnes: List[Alumne]):
    with open(FITXER_ALUMNES, "w") as f:
        json.dump([alumne.dict() for alumne in alumnes], f, indent=4)

# Ruta principal
@app.get("/")
def llegir_institut():
    return {"missatge": "Institut TIC de Barcelona"}

# Ruta per obtenir el nombre total d'alumnes
@app.get("/alumnes/")
def obtenir_numero_alumnes():
    alumnes = llegir_dades()
    return {"total_alumnes": len(alumnes)}

# Ruta per obtenir les dades d'un alumne per ID
@app.get("/id/{id}")
def obtenir_alumne(id: int):
    alumnes = llegir_dades()
    alumne = next((a for a in alumnes if a["id"] == id), None)
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

# Ruta per esborrar un alumne per ID
@app.delete("/del/{id}")
def esborrar_alumne(id: int):
    alumnes = llegir_dades()
    alumne = next((a for a in alumnes if a["id"] == id), None)
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    
    alumnes = [a for a in alumnes if a["id"] != id]
    escriure_dades([Alumne(**a) for a in alumnes])
    return {"missatge": f"Alumne amb id {id} esborrat correctament."}

# Ruta per afegir un alumne
@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    alumnes = llegir_dades()
    # Busquem el màxim ID existent
    max_id = max([a["id"] for a in alumnes], default=0)
    alumne.id = max_id + 1  # Assignem un ID nou
    alumnes.append(alumne.dict())
    escriure_dades([Alumne(**a) for a in alumnes])
    return {"missatge": "Alumne afegit correctament.", "alumne": alumne}