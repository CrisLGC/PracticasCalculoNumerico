# Clase del objeto "Cuenta"
class Cuenta:
    # Constructor del objeto "Cuenta"
    def __init__(self):
        self.__titular = None
        self.__cantidad = None
    # Funcion para retirar un monto de la cuenta    
    def retirar(self):
        while True:
            try:
                monto = float(input("Ingrese monto: "))
                break
            except ValueError:
                print("Ingrese un monto valido")
        self.__cantidad -= monto
    # Funcion para ingresar un monto de la cuenta      
    def ingresar(self):
        while True:
            try:
                monto = float(input("Ingrese monto: "))
                break
            except ValueError:
                print("Ingrese un monto valido")
        if monto>0:
            self.__cantidad += monto
        else:
            print("Ingrese un monto valido")   
    # Setters para las variables de la cuenta
    def set_t(self, nombre):
        self.__titular = nombre
    def set_c(self, cant):
        self.__cantidad=cant
    # Funcion que imprime el estado de la cuenta
    def mostrar(self):
        print("El estado de su cuenta es: ")
        print(self.__titular)
        print(self.__cantidad)
# Funcion menu
def menu():
    print("\nSeleccione lo que desea")
    print("1._ Ingresar")
    print("2._ Retirar")
    print("3._ Finalizar")
    opc = input("Seleccionar:")
    return opc
# Creacion y almacenamiento de un objeto "Cuenta" en una variable 
acc=Cuenta()
# Funcion principal
def main():
    while True:
        nombre = str(input("Ingrese el tirular: "))
        if all(parte.isalpha() for parte in nombre.split()):
            acc.set_t(nombre)
            break
        else:
            print("El nombre ingresado contiene números o símbolos. Por favor, intenta de nuevo")
    while True:
            try:
                can = float(input("Por favor, ingresa la cantidad para aperturar tu cuenta: "))
                break
            except ValueError:
                print("Ingrese un monto valido")
    while True:          
            if can >= 0:
                    acc.set_c(can)
                    acc.mostrar()
                    opc = int(menu())
                    b=True
                    while b == True:
                        if opc==1:
                            acc.ingresar()
                            acc.mostrar()
                            opc = int(menu())
                        elif opc==2:
                            acc.retirar()
                            acc.mostrar()
                            opc = int(menu())
                        elif opc==3:
                            print("*Programa finalizado*")
                            b = False 
                        else:
                            print("Por favor, ingrese una opcion valida")
                            opc = int(menu())
                    break                            
            else:
                print("El número ingresado es negativo. Por favor, ingrese una cantidad valida")
# Llamada de la funcion "main" para correr el programa
main()





    

    


    



