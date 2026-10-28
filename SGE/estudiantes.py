
# 1. MENU PRINCIPAL CON BUCLE

def menuPrincipal():

    # Bandera para controlar la salida del programa
    banderaSalir = False

    while not banderaSalir:

        print("....................................")
        print(" SISTEMA DE GESTION DE ESTUDIANTES")
        print("::::::::::::::::::::::::::::::::::::")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante por ID")
        print("4. Finalizar programa")
        print("------------------------------------")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregarEstudiante()

        elif opcion == "2":
            mostrarEstudiantes()

        elif opcion == "3":
            buscarEstudiante()

        elif opcion == "4":

            confirmar = input(
                "Desea finalizar el programa? (S/N): "
            ).strip().upper()

            if confirmar == "S":
                banderaSalir = True
                print("\nPrograma finalizado correctamente.")

            elif confirmar != "N":
                print("Respuesta invalida. Ingrese S o N.")

        else:
            print("Opcion invalida. Seleccione una opcion del 1 al 4.")


# 2. ESTRUCTURA DE DATOS PARA LOS ESTUDIANTES

# Lista dinamica para almacenar los registros
estudiantes = []

# Variable de conteo del total de estudiantes
contadorEstudiantes = 0


# 3. FUNCION PARA AGREGAR ESTUDIANTES

def agregarEstudiante():
    global contadorEstudiantes

    print("\n--- AGREGAR ESTUDIANTE ---")

    # Validar que el ID contenga unicamente numeros
    while True:

        identificacion = input(
            "Ingrese el ID del estudiante: "
        ).strip()

        if identificacion.isdigit():
            break

        else:
            print(
                "Error: el ID debe contener unicamente numeros."
            )

    # Verificar que el ID no este duplicado
    for estudiante in estudiantes:

        if estudiante["id"] == identificacion:
            print("Error: ya existe un estudiante con ese ID.")
            return

    # Solicitar y validar el nombre
    nombre = input(
        "Ingrese el nombre completo del estudiante: "
    ).strip()

    if not nombre:
        print("Error: el nombre no puede estar vacio.")
        return

    # Validar que la edad contenga unicamente numeros
    while True:

        edadTexto = input(
            "Ingrese la edad: "
        ).strip()

        if edadTexto.isdigit():

            edad = int(edadTexto)

            if 1 <= edad <= 50:
                break

            else:
                print(
                    "Error: la edad debe estar entre 1 y 50."
                )

        else:
            print(
                "Error: la edad debe contener unicamente numeros."
            )

    # Crear el diccionario con los datos del estudiante
    estudiante = {
        "id": identificacion,
        "nombre": nombre,
        "edad": edad
    }

    # Agregar el registro a la lista
    estudiantes.append(estudiante)

    # Actualizar el contador de estudiantes
    contadorEstudiantes += 1

    print("\nEstudiante agregado correctamente.")
    print(f"Total de estudiantes: {contadorEstudiantes}")


# 4. FUNCION PARA MOSTRAR UN ESTUDIANTE

def mostrarEstudiante(estudiante):

    print("------------------------------------")
    print(f"ID:     {estudiante['id']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad:   {estudiante['edad']} anios")
    print("------------------------------------")

# 5. FUNCION PARA MOSTRAR TODOS LOS ESTUDIANTES

def mostrarEstudiantes():

    print("\n--- LISTA DE ESTUDIANTES ---")

    if contadorEstudiantes == 0:
        print("No hay estudiantes registrados.")
        return

    print(f"Total de estudiantes: {contadorEstudiantes}")

    # Recorrer la lista y mostrar cada estudiante
    for estudiante in estudiantes:
        mostrarEstudiante(estudiante)

    print("------------------------------------")


# 6. FUNCION PARA BUSCAR UN ESTUDIANTE POR ID

def buscarEstudiante():

    print("\n--- BUSCAR ESTUDIANTE POR ID ---")

    if contadorEstudiantes == 0:
        print("No hay estudiantes registrados para buscar.")
        return

    # Validar que el ID de busqueda contenga solo numeros
    while True:

        identificacion = input(
            "Ingrese el ID del estudiante que desea buscar: "
        ).strip()

        if identificacion.isdigit():
            break

        else:
            print(
                "Error: el ID debe contener unicamente numeros."
            )

    # Bandera para identificar si se encuentra el estudiante
    encontrado = False

    # Recorrer la lista para buscar la identificacion
    for estudiante in estudiantes:

        if estudiante["id"] == identificacion:

            print("\nEstudiante encontrado:")
            mostrarEstudiante(estudiante)

            encontrado = True
            break

    # Informar si el estudiante no existe
    if not encontrado:
        print(
            f"No se encontro un estudiante con ID "
            f"{identificacion}."
        )


# 7. INICIAR EL PROGRAMA

if __name__ == "__main__":
    menuPrincipal()
