import json

def cargar_base_datos3():
    try:
        with open("formatos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"formatos": []}
    return data

def inscribir_formato():
    # Obtener información del formato
    id_formatos = input("Ingrese el id del formato: ")
    nombre = input("Ingrese el nombre del formato: ")
   
    formatos = {
        "id": id_formatos,
        "nombre": nombre 
    }

    try:
        with open("formatos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"formatos": []}

    data["formatos"].append(formatos)

    with open("formatos.json", "w") as file:
        json.dump(data, file, indent=2)

    print("formato inscrito exitosamente.")



def enlistar_formatos():
    data = cargar_base_datos3()

    if data["formatos"]:
        print("Listado de formatos inscritos:")
        for formatos in data["formatos"]:
            print(f"ID: {formatos['id']}, Nombre: {formatos['nombre']}")
    else:
        print("No hay formatos inscritos.")

