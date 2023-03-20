"""
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
    persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
    opcional. Crear los siguientes métodos para la clase:
    - Un constructor, donde los datos pueden estar vacíos.
    - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
      directamente, sólo ingresando o retirando dinero.
    - mostrar(): Muestra los datos de la cuenta.
    - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
      negativa, no se hará nada.
    - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
      rojos.
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

cliente1 = Cuenta ("Monica")
cliente1.mostrar()
cliente1.ingresar_cantidad()
cliente1.retirar()
cliente1.mostrar()




