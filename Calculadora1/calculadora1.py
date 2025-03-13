#!/usr/bin/env python3

"""
Título de práctica: calculadora1

Descripción extendida del programa: prototipo de calculadora

Autor: yulied gabriela rojas rojas <paulina021@hotmail.com>
Fecha: 2025-03-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo
    print("Hola mundo!")
    def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre 0"

# Menú de la calculadora
print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Entrada de la opción
opcion = input("Ingresa el número de la operación (1/2/3/4): ")

# Entrada de los dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Ejecución de la operación
if opcion == '1':
    print(f"{num1} + {num2} = {sumar(num1, num2)}")
elif opcion == '2':
    print(f"{num1} - {num2} = {restar(num1, num2)}")
elif opcion == '3':
    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
elif opcion == '4':
    print(f"{num1} / {num2} = {dividir(num1, num2)}")
else:
    print("Opción no válida")

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
