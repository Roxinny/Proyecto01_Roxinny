def reporte_productos_huerta():
    # Código para reporte de productos trabajados en la huerta
    pass
    # Productos trabajados en la huerta

    tomates = int(input("Ingrese la cantidad de tomates trabajados hoy: "))
    zanahorias = int(input("Ingrese la cantidad de zanahorias trabajadas hoy: "))
    lechugas = int(input("Ingrese la cantidad de lechugas trabajadas hoy: "))

    tomates_precio_unidad = float(input("Ingrese el precio de venta por unidad de tomates en colones: "))
    zanahorias_precio_unidad = float(input("Ingrese el precio de venta por unidad de zanahorias en colones: "))
    lechugas_precio_unidad = float(input("Ingrese el precio de venta por unidad de lechugas en colones: "))

    productos = [["Producto", "Cantidad", "Precio de venta", "Monto"]]

    monto_total = 0.0

    if tomates > 0:
        monto_tomates = tomates * tomates_precio_unidad
        productos.append(["Tomates", tomates, tomates_precio_unidad, monto_tomates])
        monto_total += monto_tomates

    if zanahorias > 0:
        monto_zanahorias = zanahorias * zanahorias_precio_unidad
        productos.append(["Zanahorias", zanahorias, zanahorias_precio_unidad, monto_zanahorias])
        monto_total += monto_zanahorias

    if lechugas > 0:
        monto_lechugas = lechugas * lechugas_precio_unidad
        productos.append(["Lechugas", lechugas, lechugas_precio_unidad, monto_lechugas])
        monto_total += monto_lechugas

    # Mostramos al usuario la lista de productos trabajados y sus precios en caso de estar en término para vender
    for i in range(len(productos)):
        print("{:<12} {:<10} {:<20} ${:<10}".format(*productos[i]))

    print("Monto total: ${}".format(monto_total))

    producto_eliminar = input("Ingrese el nombre del producto a eliminar")
    encontrado = False
    for i in range(1, len(productos)):
        if productos[i][0] == producto_eliminar:
            encontrado = True
            print("{:<12} {:<10} {:<20} ${:<10}".format(*productos[i]))

            confirmar = input("¿Está seguro de que desea eliminar este producto? (S/N): ").upper()
            if confirmar == "S":
                monto_total -= productos[i][3]
                productos.pop(i)
                print("El producto se ha eliminado exitosamente.")
                print()
                break
            else:
                print("Operación cancelada.")
                print()

    if not encontrado:
        print("El producto no se ha encontrado.")
        print()

    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opción inválida. Intente nuevamente.")
        print()

        # Mostramos al usuario la lista de productos trabajados y sus precios en caso de estar en término para vender
    for i in range(len(productos)):
        print("{:<12} {:<10} {:<20} ${:<10}".format(*productos[i]))

        print("Monto total: ${}".format(monto_total))
    else:
        print("Opción inválida. Intente nuevamente.")

    input("Presione enter para continuar ...")
