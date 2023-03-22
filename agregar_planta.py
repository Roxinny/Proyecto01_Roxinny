def agregar_planta():
    # Código para agregar planta
    pass
    # Pedimos al usuario que ingrese los datos necesarios para realizar los cálculos
    num_plantas = int(input("Ingrese el número de plantas que se deben regar: "))

    # Creamos una lista vacía donde guardaremos los datos de cada planta
    plantas = []

    # Pedimos los datos de cada planta y los agregamos a la lista
    for i in range(num_plantas):
        print(f"Datos de la planta #{i + 1}:")
        tipo_suelo = input("Tipo de suelo (arcilloso, arenoso o mixto): ")
        tamano = float(input("Tamaño de la planta (en metros cuadrados): "))
        plantas.append((tipo_suelo, tamano))

    # Definimos una función para calcular la cantidad de agua que necesita cada planta
    def calcular_agua(tipo_suelo, tamano):
        if tipo_suelo == "arcilloso":
            return tamano * 0.3
        elif tipo_suelo == "arenoso":
            return tamano * 0.5
        elif tipo_suelo == "mixto":
            return tamano * 0.4

    # Mostramos la cantidad de agua que necesita cada planta
    print("Cantidad de agua que necesita cada planta:")
    for i, planta in enumerate(plantas):
        tipo_suelo, tamano = planta
        agua_necesaria = calcular_agua(tipo_suelo, tamano)
        print(f"Planta #{i + 1}: {agua_necesaria} litros")

        input("Presione enter para continuar ...")