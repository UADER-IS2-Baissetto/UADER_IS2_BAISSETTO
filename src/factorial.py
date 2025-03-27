#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                         *
#* Calcula el factorial de un número o rango de números usando OOP          *
#* Dr.P.E.Colla (c) 2022                                                    *
#* Creative commons                                                         *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        # Constructor vacío (en caso de que quieras agregar atributos más tarde)
        pass

    def factorial(self, num):
        """Calcula el factorial de un número individual."""
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        """Calcula el factorial de todos los números entre min y max (inclusive)."""
        for num in range(min, max + 1):
            print(f"El factorial de {num} es: {self.factorial(num)}")

# Función principal que maneja los argumentos y la lógica de ejecución
def main():
    if len(sys.argv) > 1:
        try:
            # Extraer el valor del rango y comprobar el formato
            if sys.argv[1].startswith("-"):
                # Caso en el que se pasa "-hasta", ej: "-10"
                hasta = int(sys.argv[1][1:])  # Elimina el guion y convierte el número
                desde = 1
            elif sys.argv[1].endswith("-"):
                # Caso en el que se pasa "desde-", ej: "5-"
                desde = int(sys.argv[1][:-1])  # Elimina el guion y convierte el número
                hasta = 60
            else:
                # Caso en el que se pasa "desde-hasta", ej: "4-8"
                rango = sys.argv[1].split('-')
                if len(rango) != 2:
                    raise ValueError("El formato del argumento debe ser 'desde-hasta' o '-hasta' o 'desde-'.")

                desde = int(rango[0])
                hasta = int(rango[1])

        except (ValueError, IndexError):
            print("El argumento proporcionado no es válido. Asegúrese de usar el formato correcto.")
            sys.exit()
    else:
        # Si no se pasa un rango, solicitamos uno
        rango = input("Ingrese el rango (ej. 4-8, -10 o 5-): ").split('-')
        try:
            if len(rango) == 1 and rango[0].startswith("-"):
                hasta = int(rango[0][1:])  # Elimina el guion y convierte el número
                desde = 1
            elif len(rango) == 1 and rango[0].endswith("-"):
                desde = int(rango[0][:-1])  # Elimina el guion y convierte el número
                hasta = 60
            elif len(rango) == 2:
                desde = int(rango[0])
                hasta = int(rango[1])
            else:
                raise ValueError("El formato debe ser 'desde-hasta', '-hasta' o 'desde-'.")
        except ValueError:
            print("El rango ingresado no es válido. Asegúrese de usar el formato correcto.")
            sys.exit()

    # Crear una instancia de la clase Factorial y ejecutar el cálculo
    factorial_calculator = Factorial()
    factorial_calculator.run(desde, hasta)

# Llamar a la función principal
if __name__ == "__main__":
    main()