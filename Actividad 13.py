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

