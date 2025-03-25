import os
import json

# Variables
nom_fitxer = "alumnes.json"

# Classe Alumne per organitzar les dades
class Alumne:
    def __init__(self, id, nom, cognom, dia, mes, any, email, feina, curs):
        self.id = id
        self.nom = nom
        self.cognom = cognom
        self.data = {"dia": dia, "mes": mes, "any": any}
        self.email = email
        self.feina = feina
        self.curs = curs

    def __str__(self):
        return f"{self.id} - {self.nom} {self.cognom}"

# Funció per llegir els alumnes des de JSON
def llegir_alumnes():
    try:
        with open(nom_fitxer, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Funció per guardar els alumnes en JSON
def desar_alumnes(alumnes):
    with open(nom_fitxer, "w") as f:
        json.dump([alumne.__dict__ for alumne in alumnes], f, indent=4)

# Funció per generar un ID únic
def generar_id(alumnes):
    return max([alumne.id for alumne in alumnes], default=0) + 1

# Funció per mostrar tots els alumnes
def mostrar_alumnes(alumnes):
    if not alumnes:
        print("No hi ha alumnes registrats.")
    else:
        for alumne in alumnes:
            print(f"{alumne.id} - {alumne.nom} {alumne.cognom}")

# Funció per veure un alumne per ID
def veure_alumne(alumnes, id):
    for alumne in alumnes:
        if alumne.id == id:
            return alumne
    return None

# Funció per esborrar un alumne per ID
def esborrar_alumne(alumnes, id):
    for i, alumne in enumerate(alumnes):
        if alumne.id == id:
            del alumnes[i]
            return True
    return False

# Funció per afegir un alumne
def afegir_alumne(alumnes):
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    dia = int(input("Dia de naixement: "))
    mes = int(input("Mes de naixement: "))
    any = int(input("Any de naixement: "))
    email = input("Email: ")
    feina = input("Feina (True/False): ") == "True"
    curs = input("Curs: ")
    
    id = generar_id(alumnes)
    alumne = Alumne(id, nom, cognom, dia, mes, any, email, feina, curs)
    alumnes.append(alumne)

# Funció per mostrar el menú
def menu():
    os.system('cls')
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")
    print("\n0. Sortir\n\n\n")
    print(">", end=" ")
    return input()

# Programa principal
def programa():
    alumnes = []
    while True:
        opcio = menu()
        
        match opcio:
            case "1":
                os.system('cls')
                print("Mostrar alumnes")
                print("-------------------------------")
                mostrar_alumnes(alumnes)
                input()

            case "2":
                os.system('cls')
                print("Afegir alumne")
                print("-------------------------------")
                afegir_alumne(alumnes)
                print("Alumne afegit correctament.")
                input()

            case "3":
                os.system('cls')
                print("Veure alumne")
                print("-------------------------------")
                id = int(input("ID de l'alumne: "))
                alumne = veure_alumne(alumnes, id)
                if alumne:
                    print(f"ID: {alumne.id}\nNom: {alumne.nom}\nCognom: {alumne.cognom}\nData: {alumne.data['dia']}/{alumne.data['mes']}/{alumne.data['any']}\nEmail: {alumne.email}\nFeina: {alumne.feina}\nCurs: {alumne.curs}")
                else:
                    print("Alumne no trobat.")
                input()

            case "4":
                os.system('cls')
                print("Esborrar alumne")
                print("-------------------------------")
                id = int(input("ID de l'alumne a esborrar: "))
                if esborrar_alumne(alumnes, id):
                    print("Alumne esborrat correctament.")
                else:
                    print("Alumne no trobat.")
                input()

            case "5":
                os.system('cls')
                print("Desar a fitxer")
                print("-------------------------------")
                desar_alumnes(alumnes)
                print("Dades desades al fitxer.")
                input()

            case "6":
                os.system('cls')
                print("Llegir fitxer")
                print("-------------------------------")
                alumnes = llegir_alumnes()
                print("Dades llegides del fitxer.")
                input()

            case "0":
                os.system('cls')
                print("Adeu!")
                break

            case _:
                os.system('cls')
                print("Opció incorrecta\n")
                input()

if __name__ == "__main__":
    programa()
