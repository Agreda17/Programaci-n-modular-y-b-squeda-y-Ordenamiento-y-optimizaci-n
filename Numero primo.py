def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def ingresar_valor():
    while True:
        valor = input("Ingrese un número : ")
        if valor.lower() == 'salir':
            return None
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print("Error: Ingrese un número válido.")

def encontrar_primo():
    while True:
        numero = ingresar_valor()
        if numero is None:
            print("Programa finalizado.")
            break
        if es_primo(numero):
            print(f"El número {numero} es primo.")
            break

encontrar_primo()

