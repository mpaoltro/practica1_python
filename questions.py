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
word = random.choice(words)
guessed = []
attempts = 6
score = 0  # Variable para llevar la puntuación del jugador, se incrementa por cada letra correcta adivinada
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        score += 6  # Suma por ganar
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    
    # Validar entrada: debe ser una sola letra y no un número o símbolo 
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
        score -= 1  # Resta por error
        print("Esa letra no está en la palabra.")
        
    print()
    
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0  # Pierde con 0 puntos
    
print(f"Tu puntuación final es: {score}") # Mostrar puntaje final al finalizar el juego