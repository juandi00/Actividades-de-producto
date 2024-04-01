def main():
    contraseña_correcta = "1234"
    contraseña_ingresada = ""

    while contraseña_ingresada != contraseña_correcta:
        contraseña_ingresada = input("Ingrese la contraseña: ")
        if contraseña_ingresada != contraseña_correcta:
            print("Contraseña incorrecta. Inténtelo nuevamente.")

    print("¡Bienvenido!")

if __name__ == "__main__":
    main()