class ValidadorContraseña:
    def validar(self, contraseña, longitud_minima):
        try:
            if len(contraseña) >= longitud_minima:
                return True
            else:
                return False
        except TypeError:
            return False


validador = ValidadorContraseña()
contraseña = input("Ingrese una contraseña: ")
longitud_minima = 8

if validador.validar(contraseña, longitud_minima):
    print("La contraseña cumple con la longitud mínima requerida.")
else:
    print("La contraseña no cumple con la longitud mínima requerida.")
