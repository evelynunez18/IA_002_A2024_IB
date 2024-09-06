import random

def adivina_el_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0

    print("He generado un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        try:
            intento = int(input("¿Qué número crees que es? "))
            intentos += 1

            if intento < 1 or intento > 100:
                print("Por favor, elige un número entre 1 y 100.")
            elif intento < numero_aleatorio:
                print("El número es mayor. Intenta de nuevo.")
            elif intento > numero_aleatorio:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()
