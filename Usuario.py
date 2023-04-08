from datetime import date #esto es para la fecha
class Usuario:
    def __init__(self,Id:int,Nombres:str, Apellidos:str,Genero:str, Fecha_Nacimiento:date, Rut:str):
        self.__Id=Id
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Genero=Genero
        self.__Fecha_Nacimiento=Fecha_Nacimiento    #DateTime
        self.__Rut=Rut
        self.__Cargo = []
        pass

    #GETTERS
    def get_id(self):
        return self.__Id

    def get_nombres(self):
        return self.__Nombres

    def get_apellidos(self):
        return self.__Apellidos

    def get_genero(self):
        return self.__Genero

    def get_fecha_nacimiento(self):
        return self.__Fecha_Nacimiento

    def get_rut(self):
        return self.__Rut

    def get_cargo(self):
        return self.__Cargo #revisar luego

    #SETTERS
    # Nombre, apellido, genero fecha_nacimiento y rut inesesario ????????

    def set_id(self):
        self.__Id = int(input("Ingrese nuevo id: "))

    def set_cargo(self):
        #Aca añadir, eliminar o modificar cargos
        pass


#probando codigo
#recordar colocar date en las fechas, (año,mes,dia)
test=Usuario(123,"juan","soto","hombre",date(1999,10,2),12345678)
test.get_id()
test.get_nombres()
test.get_apellidos()
test.get_genero()
test.get_fecha_nacimiento()
test.get_rut()
