#Para importar las clases
from clientes import cliente
from equipos import equipo

#Crear clientes y equipos
cliente1 = cliente()
equipo1 = equipo()

opcion = 0

while (opcion != 5):
    print("1. Agregar clinete.")
    print("2. Crear equipo.")
    print("3. Asignar equipo a cliente.")
    print("4. Ver listadod equipos.")
    print("5. Salir.")
    print("-*50")

    opcion = int(input("Ingrese la opcion que desea: "))

    if opcion == 1:
        #Pedidr datos del cliente
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        numero = input("Ingrese el numero del cliente: ")

        #Agregar cliente
        cliente1.Agregar_Cliente(nombre, apellido, numero)

    elif opcion == 2:
        #Ingresar los datos del equipo    
        codigo = input("Ingrese el codigo del equipo: ")
        nombreEquipo = input("Ingrese el nombre del equipo: ")
        precio = float(input("Ingrese el precio del equipo: "))

        #Agregar equipo
        equipo1.Agregar_Equipo(codigo, nombreEquipo, precio)

    elif opcion == 3:
        cliente1.Agregar_Equipo(equipo1)

    elif opcion == 4:
        cliente1.Ver_Equipos()
