import json

def cargar_base_datos4():
    try:
        with open("peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": []}
    return data

def agregar_peliculas():
    # Obtener información del formato
    id_peliculas = input("Ingrese el id de la pelicula: ")
    nombre = input("Ingrese el nombre de la pelicula: ")
    duracion= input("Ingrese la duracion")
    sinopsis= input ("Ingrese la sinopsis")
    
   
    peliculas = {
        "id": id_peliculas,
        "nombre": nombre,
        "duracion": duracion,
        "sinopsis": sinopsis 
    }

    try:
        with open("peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": []}

    data["peliculas"].append(peliculas)

    with open("peliculas.json", "w") as file:
        json.dump(data, file, indent=2)

    print("pelicula inscrita exitosamente.")
    
    
def editar_peliculas():
    id_a_modificar = input("Ingrese el ID de la película a modificar: ")

    data = cargar_base_datos4()

    encontrada = False
    for pelicula in data["peliculas"]:
        if pelicula["id"] == id_a_modificar:
            encontrada = True
            print(f"Modificar película con ID: {id_a_modificar}")
            pelicula["nombre"] = input("Nuevo nombre de la película: ")
            pelicula["duracion"] = input("Nueva duración de la película: ")
            pelicula["sinopsis"] = input("Nueva sinopsis de la película: ")
            break

    if encontrada:
        with open("peliculas.json", "w") as file:
            json.dump(data, file, indent=2)
        print("Película modificada exitosamente.")
    else:
        print(f"No se encontró ninguna película con el ID {id_a_modificar}.")

def eliminar_peliculas():
    id_a_eliminar = input("Ingrese el ID de la película a eliminar: ")

    data = cargar_base_datos4()

    encontrada = False
    for pelicula in data["peliculas"]:
        if pelicula["id"] == id_a_eliminar:
            encontrada = True
            data["peliculas"].remove(pelicula)
            break

    if encontrada:
        with open("peliculas.json", "w") as file:
            json.dump(data, file, indent=2)
        print("Película eliminada exitosamente.")
    else:
        print(f"No se encontró ninguna película con el ID {id_a_eliminar}.")

def buscar_peliculas():
    termino_busqueda = input("Ingrese el término de búsqueda: ")

    data = cargar_base_datos4()

    encontradas = []
    for pelicula in data["peliculas"]:
        if termino_busqueda.lower() in pelicula["nombre"].lower() or termino_busqueda.lower() in pelicula["sinopsis"].lower():
            encontradas.append(pelicula)

    if encontradas:
        print("Películas encontradas:")
        for pelicula_encontrada in encontradas:
            print(f"ID: {pelicula_encontrada['id']}, Nombre: {pelicula_encontrada['nombre']}")
    else:
        print("No se encontraron películas que coincidan con el término de búsqueda.")

def enlistar_peliculas():
    data = cargar_base_datos4()

    if data["peliculas"]:
        print("Listado de películas inscritas:")
        for pelicula in data["peliculas"]:
            print(f"ID: {pelicula['id']}, Nombre: {pelicula['nombre']}, Duración: {pelicula['duracion']}, Sinopsis: {pelicula['sinopsis']}")
    else:
        print("No hay películas inscritas.")
        
     
    
