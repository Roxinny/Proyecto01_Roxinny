def planificacion_siembra():
    # Código para planificación de siembra
    pass
    # Definir los productos que siembra el colegio
    productos_colegio = ["tomate", "cebolla", "zanahoria", "lechuga", "pepino"]

    # Mostrar los productos disponibles al usuario
    print("Los productos disponibles para sembrar son: {}".format(", ".join(productos_colegio)))

    # Solicitar al usuario que ingrese el producto que desea sembrar
    producto = input("Ingrese el producto que desea sembrar: ")

    # Validar si el producto está en la lista de productos del colegio
    if producto in productos_colegio:
        # Si el producto es uno de los productos del colegio, mostrar la mejor época para sembrarlo
        if producto == "tomate":
            epoca_siembra = "Octubre - Noviembre"
        elif producto == "cebolla":
            epoca_siembra = "Marzo - Abril"
        elif producto == "zanahoria":
            epoca_siembra = "Agosto - Septiembre"
        elif producto == "lechuga":
            epoca_siembra = "Marzo - Abril y Agosto - Septiembre"
        elif producto == "pepino":
            epoca_siembra = "Octubre - Noviembre y Marzo - Abril"

        # Mostrar la mejor época para sembrar el producto
        print("                                     ")
        print("La mejor época para sembrar {} es en {}.".format(producto, epoca_siembra))

    else:
        # Si el producto no está en la lista de productos del colegio, mostrar un mensaje de error
        print("Lo siento, el producto que ingresó no está en la lista de productos del colegio.")

