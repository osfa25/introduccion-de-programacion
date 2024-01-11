import json

def cargar_base_datos2():
    try:
        with open("actores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"actores": []}
    return data

def inscribir_actor():
    # Obtener información del actor
    id_actor = input("Ingrese el id del actor: ")
    nombre = input("Ingrese el nombre del actor: ")
   
    actores = {
        "id": id_actor,
        "nombre": nombre 
    }

    try:
        with open("actores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"actores": []}

    data["actores"].append(actores)

    with open("actores.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Actor inscrito exitosamente.")
    



def enlistar_actores():
    data = cargar_base_datos2()

    if data["actores"]:
        print("Listado de actores inscritos:")
        for actores in data["actores"]:
            print(f"ID: {actores['id']}, Nombre: {actores['nombre']}")
    else:
        print("No hay actores inscritos.")

def eliminar_actores():
    id_a_eliminar = input("Ingrese el ID del actor a eliminar: ")

    data = cargar_base_datos2()

    encontrada = False
    for actor in data["actores"]:
        if actor["id"] == id_a_eliminar:
            encontrada = True
            data["actores"].remove(actor)
            break

    if encontrada:
        with open("actores.json", "w") as file:
            json.dump(data, file, indent=2)
        print("Actor eliminado exitosamente.")
    else:
        print(f"No se encontró ningún actor con el ID {id_a_eliminar}.")

