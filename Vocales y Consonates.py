def contar_vocales_consonantes(frase):
    vocales = 0
    consonantes = 0
    vocales_contador = {}
    consonantes_contador = {}

    for letra in frase:
        if letra.isalpha():
            if letra.lower() in 'aeiou':
                vocales += 1
                if letra.lower() in vocales_contador:
                    vocales_contador[letra.lower()] += 1
                else:
                    vocales_contador[letra.lower()] = 1
            else:
                consonantes += 1
                if letra.lower() in consonantes_contador:
                    consonantes_contador[letra.lower()] += 1
                else:
                    consonantes_contador[letra.lower()] = 1

    print("Recuento de vocales:")
    for vocal, count in vocales_contador.items():
        print(f"{vocal}: {count}")

    print("Recuento de consonantes:")
    for consonante, count in consonantes_contador.items():
        print(f"{consonante}: {count}")

    if vocales > consonantes:
        print("La frase tiene más vocales que consonantes.")
        print(f"Vocales: {vocales} Consonantes: {consonantes}")
    elif consonantes > vocales:
        print("La frase tiene más consonantes que vocales.")
        print(f"Vocales: {vocales} Consonantes: {consonantes}")
    else:
        print("La frase tiene la misma cantidad de vocales y consonantes.")
        print(f"Vocales: {vocales} Consonantes: {consonantes}")

frase = input("Ingrese una frase: ")
contar_vocales_consonantes(frase)
