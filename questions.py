import random

categories = {
    "programacion": ["python", "programa", "variable", "funcion"],
    "conceptos": ["bucle", "cadena", "entero", "lista"]
}

print("Categorías disponibles:")
for categoria in categories:
    print("-", categoria)

choice = input("Elegí una categoría: ")

if choice not in categories:
    print("Categoría no válida.")
    exit()

words = categories[choice]

# Mezcla sin repetir
shuffled_words = random.sample(words, len(words))

index = 0
score = 0

print("¡Bienvenido al Ahorcado!")
print()

while True:
    # Si no quedan palabras
    if index >= len(shuffled_words):
        print("No quedan más palabras.")
        break

    word = shuffled_words[index]
    index += 1

    guessed = []
    attempts = 6

    print("Nueva ronda!")

    while attempts > 0:
        progress = ""

        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        # Validación
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida.")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0

    print(f"Puntaje actual: {score}")

    seguir = input("¿Querés jugar otra ronda? (s/n): ").lower()
    if seguir != "s":
        break

print(f"Tu puntuación final es: {score}")