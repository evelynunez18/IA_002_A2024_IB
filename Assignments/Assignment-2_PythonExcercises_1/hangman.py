import random

def elegir_palabra():
    palabras = ['python', 'programacion', 'hangman', 'desarrollo', 'computadora']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    return ' '.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos = 6

    print("¡Bienvenido al juego del Hangman!")
    
    while intentos > 0:
        print("\nPalabra:", mostrar_estado(palabra, letras_adivinadas))
        print(f"Tienes {intentos} intentos restantes.")
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta de nuevo.")
            continue

        letras_adivinadas.add(letra)

        if letra not in palabra:
            intentos -= 1
            print("Letra incorrecta.")
        
        if all(letra in letras_adivinadas for letra in palabra):
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break
    else:
        print("\n¡Perdiste! La palabra era:", palabra)

if __name__ == "__main__":
    jugar()
