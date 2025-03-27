#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o rango de números                    *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Función para calcular factoriales de un rango
def calcular_factoriales_desde_hasta(desde, hasta):
    for num in range(desde, hasta + 1):
        print(f"El factorial de {num} es: {factorial(num)}")

# Verificar si el rango ha sido pasado como argumento
if len(sys.argv) > 1:
    try:
        # Extraer los valores del rango (formato "desde-hasta")
        rango = sys.argv[1].split('-')
        if len(rango) != 2:
            raise ValueError("El formato del argumento debe ser 'desde-hasta'.")

        desde = int(rango[0])
        hasta = int(rango[1])

    except (ValueError, IndexError):
        print("El argumento proporcionado no es válido. Asegúrese de usar el formato 'desde-hasta'.")
        sys.exit()
else:
    # Si no se pasa un rango, solicitamos uno
    rango = input("Ingrese el rango (ej. 4-8): ").split('-')
    try:
        if len(rango) != 2:
            raise ValueError("El formato debe ser 'desde-hasta'.")
        
        desde = int(rango[0])
        hasta = int(rango[1])
    except ValueError:
        print("El rango ingresado no es válido. Asegúrese de usar el formato 'desde-hasta'.")
        sys.exit()