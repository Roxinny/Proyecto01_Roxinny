
# Proyecto No.1 - Individual
# Estudiante: Roxinny Jimenez Vega
#  Resolusion de Problemas Sistema de Control de Riego en CTP de Matapalo.



class SistemaRiego:
    _instance = None

    def __init__(self):
        self.nombre = "soy unico"

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def getInstance():
        if SistemaRiego._instance is None:
            SistemaRiego._instance = SistemaRiego()
        return SistemaRiego._instance


        # Inicializar el sistema de riego
        sistema = SistemaRiego.getInstance()

