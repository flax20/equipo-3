from datetime import date

class Cliente:
    def __init__(self, id: int, nombres:str, apellidos:str, genero: str, Fecha_Nacimiento:date, email:str, rut: str, telefono: str, domicilio: str):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__Fecha_Nacimiento =  Fecha_Nacimiento #Para el DateTime
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
    
    def get_Mascota(self,i):
         return self.__mascotas[i]
    
    def get_Historiales(self,i):        #Crear Variable i?
        return print(self.__historial[i])
    

            #Setters

    def set_Mail(self):
         self.__email = str(input(" Ingrese mail nuevo : "))

    def set_Telefono(self):
         self.__telefono = str(input(" Ingrese telefono nuevo : "))

    def set_Domicilio(self):
         self.__domicilio = str(input(" Ingrese domicilio nuevo : "))

    def set_Mscotas(self,mascotas):
        self.__mascotas = mascotas          #Pregunta profe ¿Que pasa si quiere modificar una mascotas, si es un arreglo?

    def set_Historial(self,historial):
        self.__historial = historial        #Tal vez hay que sacarlo
