estudiantes = {}
def ingresar_estudiante():
    id_estudiante = input("Ingrese el ID del estudiante: ")
    if id_estudiante in estudiantes:
        print("Ese ID ya está registrado, vuelva a ingresarlo")
        return
    nombre = input("Ingrese el nombre completo del estudiante: ")
    carrera = input("Ingrese la carrera o programa académico que cursa: ")
    estudiantes[id_estudiante] = {"Nombre": nombre, "Carrera": carrera, "Cursos": {}}
    print("Se ha agregado al estudiante correctamente")
def agregar_curso():
    while True:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        if id_estudiante not in estudiantes:
            print("El ID que ingresó no fue encontrado")
        elif id_estudiante in estudiantes:
            break
    curso = input("Ingrese el nombre del curso: ")
    try:
        nota = float(input("Ingrese la nota final (0 a 100): "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
    except Exception as e:
        print("Se produjo un error inesperado:", e)
    else:
        if 0 <= nota <= 100:
            estudiantes[id_estudiante]['Cursos'][curso] = nota
            print("Se ha agregado el curso y la nota del estudiante")
        else:
            print("La nota debe ser mayor o igual a 0 y menor o igual a 100")
def consultar_estudiante():
    while True:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        if id_estudiante not in estudiantes:
            print("El ID no fue encontrado, vuelva a intentar")
        if id_estudiante in estudiantes:
            break
    datos = estudiantes[id_estudiante]
    print(f"\nNombre: {datos['Nombre']}")
    print(f"Carrera: {datos['Carrera']}")
    if datos["Cursos"]:
        print("Cursos y notas:")
        for curso, nota in datos["Cursos"].items():
            print(f"  {curso}: {nota}\n")
def calcular_promedio(estudiantes):
    id_estudiante = input("Ingrese el ID del estudiante: ")
    while True:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        if id_estudiante not in estudiantes:
            print("El ID no fue encontrado, vuelva a intentar")
        elif id_estudiante in estudiantes:
            break
    cursos = estudiantes[id_estudiante]["Cursos"]
    if cursos:
        promedio = sum(cursos.values()) / len(cursos)
        print(f"Promedio de {estudiantes[id_estudiante]['Nombre']}: {promedio:.2f}\n")
    else:
        print("No hay cursos registrados")
def aprobado(estudiantes):
    while True:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        if id_estudiante not in estudiantes:
            print("El ID no fue encontrado, vuelva a intentar")
        if id_estudiante in estudiantes:
            break
    cursos = estudiantes[id_estudiante]["Cursos"]
    if cursos:
        aprobados = all(nota >= 61 for nota in cursos.values())
        if aprobados:
            print("Todos los cursos están aprobados")
        else:
            print("No aprobó todos los cursos")
    else:
        print("No hay cursos registrados.")
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    for id_estudiantes, datos in estudiantes.items():
        print(f"\nID: {id_estudiantes}")
        print(f"Nombre: {datos['Nombre']}")
        print(f"Carrera: {datos['Carrera']}")
        if datos["Cursos"]:
            print("Cursos y notas:")
            for curso, nota in datos["Cursos"].items():
                print(f"  {curso}: {nota}")
        else:
            print("Sin cursos registrados")
while True:
    print("---GESTIÓN ACADÉMICA---\n"
          "1.- Agregar estudiante\n"
          "2.- Agregar curso con nota\n"
          "3.- Consultar notas\n"
          "4.- Calcular promedio de estudiante\n"
          "5.- Verificar si aprueba\n"
          "6.- Mostrar todos los estudiantes\n"
          "7.- Salir del programa")
    opciones = input("Escriba el número de opción que desea seleccionar: ")
    print("\n")
    match opciones:
        case "1":
            print("---AGREGAR ESTUDIANTE---\n")
            ingresar_estudiante()
        case "2":
            print("---AGREGAR CURSO CON NOTA---\n")
            agregar_curso()
        case "3":
            print("---CONSULTAR ESTUDIANTE---\n")
            consultar_estudiante()
        case "4":
            print("---CALCULAR PROMEDIO DE UN ESTUDIANTE---\n")
            calcular_promedio(estudiantes)
        case "5":
            print("---VERIFICAR SI EL ESTUDIANTE APRUEBA---\n")
            aprobado(estudiantes)
        case "6":
            print("---MOSTRAR TODOS LOS ESTUDIANTES---\n")
            mostrar_estudiantes(estudiantes)
        case "7":
            print("Programa terminado, gracias por utilizarlo...")
            break
        case _:
            print("Opción inválida, vuelva a seleccionar la opción que desea")