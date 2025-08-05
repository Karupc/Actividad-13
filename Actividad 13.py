estudiantes = {}
def ingresar_estudiante():
    id_estudiante = input("Ingrese el ID del estudiante: ")
    if id_estudiante in estudiantes:
        print("Ese ID ya está registrado, vuelva a ingresarlo")
        return
    nombre = input("Ingrese el nombre completo del estudiante: ")
    carrera = input("Ingrese la carrera o programa académico que cursa: ")
    estudiantes[id_estudiante] = {"Nombre": nombre, "Carrera": carrera, "Cursos:": {}}
    print("Se ha agregado al estudiante correctamente")
def agregar_curso():
    id_estudiante = input("Ingrese el ID del estudiante: ")
    if id_estudiante not in estudiantes:
        print("El ID que ingresó no fue encontrado")
        return
    curso = input("Ingrese el número del curso: ")
    nota = float(input("Ingrese la nota final (0 a 100): "))
    if 0 <= nota <= 100:
        estudiantes[id_estudiante]["Cursos"][curso] = nota
        print("Se ha agregado el curso y la nota del estudiante")
    else:
        print("La nota debe ser mayor o igual a 0 y menor o igual a 100")
def consultar_estudiante():
    id_estudiante = input("Ingrese el ID del estudiante: ")
    if id_estudiante in estudiantes:
        datos = estudiantes[id_estudiante]
        print(f"\nNombre: {datos['Nombre']}")
        print(f"Carrera: {datos['Carrera']}")
        if datos["Cursos"]:
            print("Cursos y notas:")
            for curso, nota in datos["Cursos"].items():
                print(f"  {curso}: {nota}")
        else:
            print("Cursos no registrados")
    else:
        print("No e encontró el ID")
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
    match opciones:
        case "1":
            print("---AGREGAR ESTUDIANTE---\n")
            ingresar_estudiante()
        case "2":
            print("---AGREGAR CURSO CON NOTA---\n")
            agregar_curso()
        case "3":
            print("---CONSULTAR ESTUDIANTE---\n")