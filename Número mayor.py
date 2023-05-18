# Solicitar al usuario tres valores numéricos
valor_1 = float(input("Ingresa el primer valor numérico: "))
valor_2 = float(input("Ingresa el segundo valor numérico: "))
valor_3 = float(input("Ingresa el tercer valor numérico: "))

# Determinar el número mayor
if valor_1 >= valor_2 and valor_1 >= valor_3:
    mayor = valor_1
elif valor_2 >= valor_1 and valor_2 >= valor_3:
    mayor = valor_2
else:
    mayor = valor_3

# Determinar el número menor
if valor_1 <= valor_2 and valor_1 <= valor_3:
    menor = valor_1
elif valor_2 <= valor_1 and valor_2 <= valor_3:
    menor = valor_2
else:
    menor = valor_3

# Determinar el número intermedio
intermedio = valor_1 + valor_2 + valor_3 - mayor - menor

# Presentar los resultados
print("El número mayor es:", mayor)
print("El número menor es:", menor)
print("El número intermedio es:", intermedio)
