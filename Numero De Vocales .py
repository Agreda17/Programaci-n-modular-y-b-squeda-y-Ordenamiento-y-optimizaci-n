frase = input("Ingresa una frase: ")  # Pedimos al usuario que ingrese una frase

vocales = 0  # Inicializamos el contador de vocales a cero

# Recorremos cada letra de la frase ingresada
for letra in frase:
    # Si la letra es una vocal, aumentamos el contador de vocales en 1
    if letra.lower() in "aeiouáéíóúü":
        vocales += 1

# Mostramos el número de vocales encontradas en la frase
print("La frase ingresada tiene", vocales, "vocales.")
