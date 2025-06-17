# Ejemplo 1: Imprimir los números del 1 al 5 usando while
print("Ejemplo 1: while del 1 al 5")
i = 1
while i <= 5:
    print(i)
    i += 1

print("-" * 40)

# Ejemplo 2: Imprimir los números del 1 al 5 usando for
print("Ejemplo 2: for del 1 al 5")
for i in range(1, 6):
    print(i)

print("-" * 40)

# Ejemplo 3: Imprimir los números del 0 al 9 usando while
print("Ejemplo 3: while del 0 al 9")
i = 0
while i < 10:
    print(i)
    i += 1

print("-" * 40)

# Ejemplo 4: Imprimir los números del 1 al 10 usando while
print("Ejemplo 4: while del 1 al 10")
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

print("-" * 40)

# Ejemplo 5: Imprimir solo los números pares del 2 al 10 usando while
print("Ejemplo 5: while pares del 2 al 10")
numero = 2
while numero <= 10:
    print(numero)
    numero += 2

print("-" * 40)

# Ejemplo 6: Imprimir los números del 0 al 9 usando for
print("Ejemplo 6: for del 0 al 9")
for i in range(10):
    print(i)

print("-" * 40)

# Ejemplo 7: Imprimir los números pares del 2 al 10 usando for
print("Ejemplo 7: for pares del 2 al 10")
for num in range(2, 11, 2):
    print(num)

print("-" * 40)

# Ejemplo 8: Imprimir los números del 1 al 5 con for usando tupla
print("Ejemplo 8: for con tupla")
for i in (1, 2, 3, 4, 5):
    print(i)

print("-" * 40)

# Ejemplo 9: Imprimir los números del 0 al 5 usando for y range(6)
print("Ejemplo 9: for con range(6)")
for i in range(6):
    print(i)

print("-" * 40)

# Ejemplo 10: for con break cuando i == 3
print("Ejemplo 10: for con break cuando i == 3")
for i in range(5):
    if i == 3:
        break  # Termina el bucle cuando i es 3
    print(i)
else:
    print("Bucle finalizado sin interrupción")  # No se ejecuta porque hubo un break

print("-" * 40)

# Ejemplo 11: Suma de dos números ingresados por el usuario
print("Ejemplo 11: suma de dos números")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
suma = numero1 + numero2
print("La suma es:", suma)

print("-" * 40)

# Ejemplo 12: Juego adivina el número
print("Ejemplo 12: Juego adivina el número")
numero_ganador = 7 
numero = int(input("Adivina el número y gana!!! Ingresa un número entre 1 y 100: "))
while numero != numero_ganador: 
    print("Lo siento, el número ingresado no es correcto. Intenta nuevamente.") 
    numero = int(input("Ingresa otro número: ")) 
print("¡Ganaste!")

print("-" * 40)

# Ejemplo 13: while contador del 1 al 5
print("Ejemplo 13: while contador del 1 al 5")
contador = 0
while contador < 5:
    contador += 1
    print(contador)

print("-" * 40)

# ==============================
# EJERCICIOS CON ERROR
# ==============================

print("EJERCICIO CON ERROR 1: Bucle infinito (NO ejecutar)")
print("""i = 1
while i <= 5:
    print(i)
""")
print("Este bucle es infinito porque nunca se incrementa el valor de i.")

print("-" * 40)

print("EJERCICIO CON ERROR 2: Incremento fuera del bucle (NO imprime correctamente)")
print("""i = 1
while i <= 5:
    print(i)
i += 1
""")
print("En este caso, el incremento está fuera del bucle. El bucle imprime solo 1 y se queda en un bucle infinito.")

print("-" * 40)

# Si quieres ver los errores en acción, descomenta y ejecuta cada bloque por separado.
