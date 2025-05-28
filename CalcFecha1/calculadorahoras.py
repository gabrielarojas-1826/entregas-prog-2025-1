from datetime import datetime, timedelta
import pytz

# Zona horaria de Colombia
colombia_tz = pytz.timezone('America/Bogota')

def mostrar_fecha_actual():
    now = datetime.now(colombia_tz)
    print(f"\n> La fecha actual es: {now}")
    return now

def calcular_nueva_fecha(fecha_actual, cantidad, unidad):
    if unidad == "segundos":
        nueva_fecha = fecha_actual + timedelta(seconds=cantidad)
    elif unidad == "dias":
        nueva_fecha = fecha_actual + timedelta(days=cantidad)
    else:
        raise ValueError("Unidad inválida")
    print(f"> La nueva fecha es: {nueva_fecha}")
    return nueva_fecha

def main():
    while True:
        fecha_actual = mostrar_fecha_actual()
        print("> Escriba 1 para ingresar segundos,\n"
              "        2 para ingresar días,\n"
              "        3 para salir.")
        opcion = input("< ")

        if opcion == "1":
            cantidad = int(input("> Escriba la cantidad de segundos\n< "))
            calcular_nueva_fecha(fecha_actual, cantidad, "segundos")
        elif opcion == "2":
            cantidad = int(input("> Escriba la cantidad de días\n< "))
            calcular_nueva_fecha(fecha_actual, cantidad, "dias")
        elif opcion == "3":
            print("> Gracias!")
            break
        else:
            print("> Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
