def reporte_riego():
    # Código para reporte de riego
    pass
    # Importar el módulo para obtener el tiempo actual
    import time

    # Solicitar al usuario los metros de terreno
    metros_terreno = int(input("Ingrese los metros de terreno de la huerta: "))

    # Solicitar al usuario la frecuencia de riego en días por semana
    dias_semana = int(input("Ingrese la cantidad de días por semana que desea regar la huerta: "))

    # Solicitar al usuario el tiempo de riego en minutos
    minutos_riego = int(input("Ingrese la cantidad de minutos que desea regar la huerta por día: "))

    # Calcular los litros de agua necesarios por día
    litros_agua = metros_terreno * 10  # 10 litros por metro cuadrado por día

    # Calcular los litros de agua necesarios por semana
    litros_semana = litros_agua * dias_semana

    # Calcular el tiempo de riego por semana en minutos
    tiempo_semana = minutos_riego * dias_semana

    # Solicitar al usuario la confirmación para regar la huerta
    confirmacion = input("¿Desea regar la huerta? (s/n): ")

    # Si el usuario confirma, mostrar los resultados
    if confirmacion == "s":
        print("Litros de agua por día:", int(litros_agua))
        print("Litros de agua por semana:", int(litros_semana))
        print("Tiempo de riego por semana (minutos):", int(tiempo_semana))
    else:
        print("No se realizará el riego.")
