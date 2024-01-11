import sys
from gestor_generos import cargar_base_datos, inscribir_genero, enlistar_generos
from gestor_actores import cargar_base_datos2, inscribir_actor, enlistar_actores, eliminar_actores
from gestor_formatos import cargar_base_datos3, inscribir_formato, enlistar_formatos
from gestor_peliculas import *
from gestor_informes import *
def mostrar_menu():
    while True:
        print("1. Aministrador de generos")
        print("2. Administrador de actores")
        print("3. Administrador de formatos")
        print("4. Gestor de peliculas")
        print("5. gestor de informes")
        print("6. Salir")
        op = input("Seleccione su opcion: ").strip()
        
        if op == "1":
            gestor_generos()  # Llamada correcta a gestor_generos()
        elif op == "2":
            gestor_actores() # Llamada correcta a gestor_actorers()
            pass
        elif op == "3":
            gestor_formatos() # gestor_formatos
            pass
        elif op == "4":
            gestor_peliculas() # gestor_peliculas
            pass
        elif op == "5":
            gestor_informes() # Lógica para gestor_informes
            pass
        elif op == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def gestor_generos():
    while True:  # Agregado para que el submenú se repita
        print("1. Crear genero")
        print("2. Listar generos")
        print("3. Ir al menu principal")
        opgestor_generos = input("Seleccione su opcion: ").strip()

        if opgestor_generos == "1":
            inscribir_genero()
        elif opgestor_generos == "2":
            enlistar_generos()
        elif opgestor_generos == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")
            
def gestor_actores():
    while True:  # Agregado para que el submenú se repita
        print("1. crear actor")
        print("2. Listar actor")
        print("3. Volver al menú principal")
        opgestor_actores = input("Seleccione su opcion: ").strip()

        if opgestor_actores == "1":
           inscribir_actor()
        elif opgestor_actores == "2":
            enlistar_actores()            
        elif opgestor_actores == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")             
            
def gestor_formatos():
    while True:  # Agregado para que el submenú se repita
        print("1. crear formato")
        print("2. Listar formato")
        print("3. Volver al menú principal")
        opgestor_formatos = input("Seleccione su opcion: ").strip()

        if opgestor_formatos == "1":
           inscribir_formato()
        elif opgestor_formatos == "2":
            enlistar_formatos()            
        elif opgestor_formatos == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida") 
            
def gestor_peliculas():
    while True:  # Agregado para que el submenú se repita
        print("1. Agregar pelicula.")
        print("2. Editar pelicula.")
        print("3. Eliminar pelicula.")
        print("4. Eliminar actor.")
        print("5. Buscar pelicula.")
        print("6. Listar todas las peliculas")
        print("7. Volver al menú principal")
        opgestor_peliculas = input("Seleccione su opcion: ").strip()

        if opgestor_peliculas == "1":
            agregar_peliculas()
        elif opgestor_peliculas == "2":
            editar_peliculas()
        elif opgestor_peliculas == "3":
            eliminar_peliculas()
        elif opgestor_peliculas == "4":
            eliminar_actores()
        elif opgestor_peliculas == "5":
            buscar_peliculas()
        elif opgestor_peliculas == "6":
            enlistar_peliculas()
        elif opgestor_peliculas == "7":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")   
            
def gestor_informes():
    while True:  # Agregado para que el submenú se repita
        print("1. Listar peliculas de un genero especifico")
        print("2. Listar peliculas donde el protagonista sea silvester stallone")
        print("3. Buscar pelicula y mostrar la sinopsis y los actores")
        print("4. Ir al menu principal")
        opgestor_informes = input("Seleccione su opcion: ").strip()

        if opgestor_informes == "1":
           enlistar_peliculas_genero()
        elif opgestor_informes == "2":
            enlistar_peliculas_actor()
        elif opgestor_informes == "3":
            buscar_mostrar_pelicula()    
        elif opgestor_informes == "4":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")                                 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
mostrar_menu()