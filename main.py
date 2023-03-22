from agregar_usuario import agregar_usuario
from reporte_productos_huerta import reporte_productos_huerta
from reporte_riego import reporte_riego
from planificacion_siembra import planificacion_siembra
from  agregar_planta import  agregar_planta
from funsiones import SistemaRiego

import os


def menu_principal():

    # Inicializar el sistema de riego
    sistema = SistemaRiego.getInstance()

    # Menú principal
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("                                     ")
        print("+++++++++++++++++++++++++++++++++++++")
        print("Sistema de riego del Colegio Matapalo")
        print("+++++++++++++++++++++++++++++++++++++")
        print("                                     ")
        print("1. Agregar usuario")
        print("2. Agregar planta")
        print("3. Productos trabajados en la huerta")
        print("4. Reporte de riego")
        print("5. Planificación de siembra:")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            agregar_planta()
        elif opcion == "3":
            reporte_productos_huerta()
        elif opcion == "4":
            reporte_riego()
        elif opcion == "5":
            planificacion_siembra()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la función menu_principal
menu_principal()




