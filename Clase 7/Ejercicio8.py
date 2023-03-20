"""
    Vamos a definir ahora una Cuenta Jovem, para ello creamos una nueva clase
    CuentaJoven que deriva de la clase creada en el punto 7. Ademas del titular 
    y la cantidad se debe guardar una bonificacion que estara expresada en
    tanto por ciento. Crear los siguientes metodos para la clase.
    -Un constructor
    -Setters y getters para el nuevo atributo
    -Titulares mayores de edad, crear un metodo es_titular_valido() que devuelve 
     verdadero si el titular es mayor de edad pero menor de 25 años y falso lo c
     contrario
    -Retiro de dinero si el titular es válido
    -Metodo mostrar() debe devolver el mensaje de "Cuenta Joven" y la bonificacion
     de la cuenta
"""
class Cuenta():
    def __init__(self, titular, cantidad=0):
        self.__titular = str(titular)
        self.__cantidad = float(cantidad)

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor

    def mostrar(self):
        print("Titular de la cuenta: " + self.titular.title())
        print("Monto en la cuenta : " + str(self.cantidad)) 

    def ingresar_cantidad(self):
        ing_valor = float(input("Monto a ingresar : "))
        if  ing_valor > 1:
            self.cantidad = ing_valor
        else : 
            print("El valor ingresado debe ser mayor a 1, vuelva a intentarlo")

    def retirar(self):
        ret_valor = float(input("Monto a retirar : "))
        self.cantidad = self.cantidad - ret_valor
        return self.cantidad
    
class Cuenta_Joven(Cuenta):
    def __init__(self, titular, cantidad, bonifica=0):
        super().__init__(titular, cantidad=0)
        self.__bonificación = bonifica
    
    @property
    def bonificación(self):
        return self.__bonificación
    
    @bonificación.setter
    def bonificación(self, valor):
        self.__bonificación = valor

    def es_titular_valido(self):
        
        edad_valida = int(input("Ingrese edad del titular : "))
        if(edad_valida >= 18) and (edad_valida < 25) :
            return True
        else :
            return False
        
            
    def retirar(self):
        if (self.es_titular_valido()):
            super().retirar()
        else :
            print("Titular no valido")


    def mostrar(self):
        print ("Cuenta Joven")
        print ("Bonificación :",self.bonificación, "%")
        

cliente2 = Cuenta_Joven("Kevin", 2)
cliente2.bonificación = 30
cliente2.retirar()
cliente2.mostrar()


