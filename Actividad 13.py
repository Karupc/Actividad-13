def ingresar_estudiante():
    id_estudiante = input("Ingrese el ID del estudiante: ")
    nombre = input("Ingrese el nombre completo del estudiante: ")
    carrera = input("Ingrese la carrera o programa académico que cursa: ")
    estudiantes[id_estudiante] = {"ID": id_estudiante, "Nombre": nombre, "Carrera": carrera}
estudiantes = {}
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
            ingresar_estudiante()

