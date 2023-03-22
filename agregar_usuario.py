def agregar_usuario():
    # Código para agregar usuario
    pass
    # Definir una lista de usuarios con sus claves y tipo de cuenta
    usuarios = [
        {'nombre': 'Yarenis', 'clave': '1612', 'tipo': 'estudiante'},
        {'nombre': 'Roxinny', 'clave': '0922', 'tipo': 'docente'}
    ]

    while True:
        print("...................................................")
        # Solicitar el ingreso de la clave al usuario
        clave_ingresada = input('Por favor ingrese su usuario: ')
        print("...................................................")

        # Buscar el usuario con la clave ingresada
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario['clave'] == clave_ingresada:
                usuario_encontrado = usuario
                break

        # Verificar si se encontró el usuario
        if usuario_encontrado is None:
            print("...................................................")

            print('Clave incorrecta. Por favor intente de nuevo.')
            print("...................................................")
        else:
            print("...................................................")

            # Mostrar el tipo de cuenta del usuario encontrado
            if usuario_encontrado['tipo'] == 'estudiante':
                print(f'Bienvenido(a) {usuario_encontrado["nombre"]}. Usted es estudiante.')
            elif usuario_encontrado['tipo'] == 'docente':
                print(f'Bienvenido(a) {usuario_encontrado["nombre"]}. Usted es docente.')
        break

    # Crear una lista vacía para almacenar los nombres de los docentes
    nombres_docentes = []

    # Solicitar al docente, nombre y apellido
    print("...................................................")
    nombre = input("Ingrese el nombre del docente: ")
    apellido = input("Ingrese el apellido del docente: ")
    print("...................................................")

    # Agregar el nombre del docente a la lista
    nombres_docentes.append(nombre + " " + apellido)

    # Mostrar la lista con los nombres de los docentes
    print("Nombres de los docentes: ")
    print("...................................................")
    print(nombres_docentes)
    print("...................................................")
    print("")

    input("Presione enter para continuar ...")
