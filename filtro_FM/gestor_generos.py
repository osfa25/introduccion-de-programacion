import json

def cargar_base_datos():
    try:
        with open("generos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"generos": []}
    return data

def inscribir_genero():
    # Obtener información del genero
    id_genero = input("Ingrese el id del genero: ")
    nombre = input("Ingrese el nombre del genero: ")
   
    genero = {
        "id": id_genero,
        "nombre": nombre
    }

    try:
        with open("generos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"generos": []}

    data["generos"].append(genero)

    with open("generos.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Genero inscrito exitosamente.")



def enlistar_generos():
    data = cargar_base_datos()

    if data["generos"]:
        print("Listado de géneros inscritos:")
        for genero in data["generos"]:
            print(f"ID: {genero['id']}, Nombre: {genero['nombre']}")
    else:
        print("No hay géneros inscritos.")
