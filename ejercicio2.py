class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad_año = int(edad)
            
            if edad_año>= 0:
                return True
            else:
                return False
        except ValueError:
            return False

# Ejemplo de uso:
validador = ValidadorDeEdad()
edad = input("Ingrese una edad: ")

if validador.validar(edad):
    print("La edad ingresada es un número entero válido.")
else:
    print("La edad ingresada no es un número entero válido o es un número negativo.")
