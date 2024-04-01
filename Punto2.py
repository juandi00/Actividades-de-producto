import random

def generar_numeros_aleatorios():
    """
    Genera dos números aleatorios entre 0 y 100.
    
    Returns:
    int: Primer número aleatorio.
    int: Segundo número aleatorio.
    """
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    return numero1, numero2

def main():
    numero1, numero2 = generar_numeros_aleatorios()
    suma_correcta = numero1 + numero2

    print(f"Por favor, calcule la suma de los siguientes dos números:")
    print(f"Número 1: {numero1}")
    print(f"Número 2: {numero2}")

    while True:
        try:
            suma_usuario = int(input("Ingrese la suma de los dos números: "))
            if suma_usuario == suma_correcta:
                print("¡Respuesta correcta!")
                break
            else:
                print("Respuesta incorrecta. Por favor, inténtelo nuevamente.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

if __name__ == "__main__":
    main()