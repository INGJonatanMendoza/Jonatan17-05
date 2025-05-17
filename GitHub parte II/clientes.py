class cliente:
    equipos = []
    
    def __init__(self):
        pass

    def Agregar_Cliente(self, nombre, apellido, numero):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numero = numero

    def Agregar_Equipo(self, equipos):
        self.equipos.append(equipos)

    def Ver_Equipos(self, equipos):
        for Mis_equipos in equipos:
            print(f"{Mis_equipos("Codigo")} {Mis_equipos("nombre")} {Mis_equipos("Precio")}")

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    

        