def mostrar_menu():
    print("\nOperaciones disponibles:")
    print("1. Pasar a minúsculas")
    print("2. Pasar a mayúsculas")
    print("3. Invertir mayúsculas / minúsculas")
    print("4. Capitalización (Primera letra mayúscula, las demás minúsculas)")
    print("5. Titulación (Primera letra mayúscula en cada palabra, las demás minúsculas)")
    print("6. Reemplazar espacios por guiones bajos")
    print("0. Salir del programa")


def main():
    texto = input("Ingrese una línea de texto arbitraria:\n")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una operación (0-6): ")

        if opcion == "1":
            texto = texto.lower()
        elif opcion == "2":
            texto = texto.upper()
        elif opcion == "3":
            texto = texto.swapcase()
        elif opcion == "4":
            texto = texto.capitalize()
        elif opcion == "5":
            texto = texto.title()
        elif opcion == "6":
            texto = texto.replace(" ", "_")
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        print("\nResultado:", texto)


if __name__ == "__main__":
    main()
