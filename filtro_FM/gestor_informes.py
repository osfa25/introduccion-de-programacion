import json
from gestor_actores import cargar_base_datos2
def cargar_base_datos4():
    try:
        with open("peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": []}
    return data

def cargar_base_datos_generos():
    try:
        with open("generos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"generos": []}
    return data

def enlistar_peliculas_genero(genero):
    data_peliculas = cargar_base_datos4()
    data_generos = cargar_base_datos_generos()

    # Buscar el ID del género
    id_genero = None
    for g in data_generos["generos"]:
        if g["nombre"].lower() == genero.lower():
            id_genero = g["id"]
            break

    if id_genero is not None:
        peliculas_genero = [p for p in data_peliculas["peliculas"] if id_genero in p.get("generos", [])]

        if peliculas_genero:
            # Crear un nuevo diccionario para el informe
            informe = {"genero": genero, "peliculas": peliculas_genero}

            # Guardar el informe en un nuevo archivo
            with open("gestion_informes.json", "w") as informes_file:
                json.dump(informe, informes_file, indent=2)

            print(f"Informe creado exitosamente para el género '{genero}' en el archivo 'gestion_informes.json'.")
        else:
            print(f"No hay películas para el género '{genero}'.")
    else:
        print(f"No se encontró el género '{genero}'.")

import json

def cargar_base_datos4():
    try:
        with open("peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": []}
    return data

def buscar_actor_por_nombre(nombre_actor):
    data_actores = cargar_base_datos2()

    for actor in data_actores["actores"]:
        if actor["nombre"].lower() == nombre_actor.lower():
            return actor["id"]

    return None

def enlistar_peliculas_actor(nombre_actor):
    id_actor = buscar_actor_por_nombre(nombre_actor)

    if id_actor is not None:
        data_peliculas = cargar_base_datos4()

        peliculas_con_actor = []
        for pelicula in data_peliculas["peliculas"]:
            if id_actor in pelicula.get("actores", []):
                peliculas_con_actor.append(pelicula)

        if peliculas_con_actor:
            print(f"Películas en las que aparece {nombre_actor}:")
            for pelicula_con_actor in peliculas_con_actor:
                print(f"ID: {pelicula_con_actor['id']}, Nombre: {pelicula_con_actor['nombre']}")
        else:
            print(f"{nombre_actor} no aparece en ninguna película.")
    else:
        print(f"No se encontró al actor {nombre_actor}.")

import json

def cargar_base_datos4():
    try:
        with open("peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": []}
    return data

def cargar_base_datos2():
    try:
        with open("actores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"actores": []}
    return data

def buscar_mostrar_pelicula(nombre_pelicula):
    data_peliculas = cargar_base_datos4()
    data_actores = cargar_base_datos2()

    encontrada = False
    for pelicula in data_peliculas["peliculas"]:
        if pelicula["nombre"].lower() == nombre_pelicula.lower():
            encontrada = True
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Sinopsis: {pelicula['sinopsis']}")
            
            if "actores" in pelicula:
                print("Actores:")
                for id_actor in pelicula["actores"]:
                    actor = next((a for a in data_actores["actores"] if a["id"] == id_actor), None)
                    if actor:
                        print(f"  - {actor['nombre']}")
            else:
                print("No hay actores asociados a esta película.")

    if not encontrada:
        print(f"No se encontró ninguna película con el nombre '{nombre_pelicula}'.")



