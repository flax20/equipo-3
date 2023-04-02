class Cliente:
    def __init__(self, id: int, nombres, apellidos, genero: str, Fecha_Nacimiento, email, rut: str, telefono: str, domicilio: str):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__Fecha_Nacimiento =  str #datetime <- eso hay que poner no se como
        self.__email = email
        self.__rut = rut
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__mascotas = []
        self.__historial = []








    #Getters 

def get_Id(self):
    return self.__id

def get_Nombres(self):
    return self.__nombres

def get_Apellidos(self):
    return self.__apellidos

def get_genero(self):
    return self.__genero

def get_FechaNacimiento(self):
    return self.__Fecha_Nacimiento

def get_Mail(self):
    return self.__email

def get_Rut(self):
    return self.__rut

def get_telefono(self):
    return self.__telefono

def get_Domicilio(self):
    return self.__domicilio

def get_Mascotas(self):
    return self.__mascotas

def get_Historial(self):
    return self.__historial

            #Setters

def set_Mail(self, email):
     self.__email = str(input("Ingrese nuevo Mail: "))

def set_Telefono(self, telefono):
     self.__telefono = str(input("Ingrese nuevo telefono:"))

def set_Domicilio(self, domicilio):
     self.__domicilio = str(input("Ingrese nuevo domicilio"))

def set_Mscotas(self,):
     self.__mascotas  #ALGO ESCRITO(POr si ascoas)

def set_(self,historial):
    return self.__historial #TIENE ARREGLO IGUAL QUE EL DE MASCOTAS Y NO SE COMO SE HACE


