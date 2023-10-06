class Divisor:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        self.resultado = None

    def realizar_division(self):
        try:
            self.resultado = self.dividendo / self.divisor
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

dividendo = float(input("Ingrese el primer número: "))
divisor = float(input("Ingrese el segundo número: "))

calculadora = Divisor(dividendo, divisor)


calculadora.realizar_division()

if calculadora.resultado is not None:
    print("El resultado de la división es:", calculadora.resultado)


