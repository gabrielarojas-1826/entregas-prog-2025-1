"""
calculadora2

Descripción extendida del programa: Prototipo de calculadora basica extendido

Autor: yulied gabriela rojas rojas <paulina021@hotmail.com>
Fecha: 2025-10-04
"""
print ('Hello World')
def obtener_operacion():
    print("\nOperaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potenciación (**)")
    print("6. División entera (//)")
    print("7. Módulo (%)")
    print("Escribe 'salir' para terminar el programa.")
    return input("¿Qué operación deseas realizar? (usa +, -, *, /, **, //, %) ").strip()

def obtener_operando(num):
    while True:
        entrada = input(f"Ingrese el operando {num} (o escriba 'cancelar' para cancelar la operación): ").strip()
        if entrada.lower() == 'cancelar':
            return None
        try:
            return float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")

def realizar_operacion(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: División por cero."
        return a / b
    elif op == '**':
        return a ** b
    elif op == '//':
        try:
            return int(a) // int(b)
        except ZeroDivisionError:
            return "Error: División por cero."
    elif op == '%':
        try:
            return int(a) % int(b)
        except ZeroDivisionError:
            return "Error: División por cero."
    else:
        return "Operación no válida."

def calculadora():
    print("Bienvenido a la calculadora interactiva.")
    while True:
        operacion = obtener_operacion()
        if operacion.lower() == 'salir':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        if operacion not in ['+', '-', '*', '/', '**', '//', '%']:
            print("Operación no reconocida. Intenta de nuevo.")
            continue
        
        op1 = obtener_operando(1)
        if op1 is None:
            print("Operación cancelada.")
            continue

        op2 = obtener_operando(2)
        if op2 is None:
            print("Operación cancelada.")
            continue

        resultado = realizar_operacion(operacion, op1, op2)
        print(f"Resultado: {resultado}")

        continuar = input("¿Deseas hacer otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
    
