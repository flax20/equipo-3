class Medicamentos:
    def __init__(self,Nombre_Medicamento:str, Descripcion:str, Precio:int, Stock:int):
        self.__Nombre_Medicamento=Nombre_Medicamento
        self.__Descripcion=Descripcion
        self.__Precio=Precio
        self.__Stock=Stock
        pass

    #GETTERS
    #Mostrar nombre del medicamento
    def get_nombre(self): 
        print (self.__Nombre_Medicamento)
    #Mostrar descripcion 
    def get_descripcion(self):
        print (self.__Descripcion)
    #Mostrar precio
    def get_precio(self):
        print (self.__Precio)
    #Mostrar stock
    def get_stock(self):
        print (self.__Stock)
    
    #SETTERS
    #modificar nombre
    def set_nombre(self):
        self.__Nombre_Medicamento = str(input("Ingrese nuevo nombre: "))
    #modificar descripcion
    def set_descripcion(self):
        self.__Descripcion = str(input("Ingrese nueva descripcion: "))
    #modificar precio
    def set_precio(self):
        #try para que se ingrese un int
        try:
            new_price= int(input("Introduce la nueva edad: "))
            #if para que el int sea mayor o igual a 0
            if new_price >= 0:
                self.__Precio=new_price
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("El precio debe ser un número entero.")

    #modificar stock
    def set_stock(self):
        try:
             new_stock = int(input("Introduce nuevo stock: "))
             if new_stock >= 0:
                  self.__Stock =new_stock
             else:
              print("El stock debe ser un número positivo.")
        except ValueError:
             print("El stock debe ser un número entero.")
             

#PROBANDO EL CODIGO
# test=Medicamentos("paracetamol", "muy bueno", 124, 6745)
# test.get_nombre()
# test.get_descripcion()
# test.get_precio()
# test.get_stock()
# test.set_stock()
# test.get_stock()
