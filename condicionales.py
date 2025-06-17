# Ejercicio 1: Verificar si eres mayor de edad (usando 19 como referencia)
edad = 19
if edad >= 19:
    print(f"Tienes {edad} años. Eres mayor de edad.")
else:
    print(f"Tienes {edad} años. Eres menor de edad.")

print("-" * 30)

# Ejercicio 2: Comparar si dos números son iguales
a = 2
b = 2
if a == b:
    print(f"a = b = {a}. Son iguales.")
else:
    print(f"a = {a}, b = {b}. Son diferentes.")

print("-" * 30)

# Ejercicio 3: Determinar si un número es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print("-" * 30)

# Ejercicio 4: Inicio de sesión sencillo
usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")
if usuario == "admin":
    if contraseña == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no reconocido.")

print("-" * 30)

# Ejercicio 5: Clasificación de la temperatura
temperatura = float(input("Ingresa la temperatura en °C: "))
if temperatura < 10:
    print("Hace mucho frío.")
elif 10 <= temperatura <= 25:
    print("El clima es agradable.")
else:
    print("Hace calor.")

print("-" * 30)

# Ejercicio 6: Comparar tres números
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))
if x == y and y == z:
    print("Los tres números son iguales.")
elif x == y or y == z or x == z:
    print("Hay dos números iguales.")
else:
    print("Todos los números son diferentes.")

print("-" * 30)

# Ejercicio 7: Determinar si un número es positivo, negativo o cero
num = float(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

print("-" * 30)

# Ejercicio 8: Encontrar el mayor de tres números
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))
if a >= b and a >= c:
    print(f"El mayor es: {a}")
elif b >= a and b >= c:
    print(f"El mayor es: {b}")
else:
    print(f"El mayor es: {c}")

print("-" * 30)

# Ejercicio 9: Clasificación de edad (usando 19)
edad_usuario = int(input("Ingrese su edad: "))
if 1 <= edad_usuario <= 12:
    print("Eres un niño.")
elif 13 <= edad_usuario <= 17:
    print("Eres un adolescente.")
elif 18 <= edad_usuario <= 19:
    print("Eres un joven adulto.")
elif 20 <= edad_usuario <= 64:
    print("Eres un adulto.")
elif 65 <= edad_usuario <= 100:
    print("Eres un adulto mayor.")
elif edad_usuario < 1:
    print("Edad no válida.")
else:
    print("Edad no válida.")

print("-" * 30)

# Ejercicio 10: Clasificación de calificación (A-F)
calificacion = float(input("Ingresa la calificación (0-100): "))
if 90 <= calificacion <= 100:
    print("Calificación: A")
elif 80 <= calificacion < 90:
    print("Calificación: B")
elif 70 <= calificacion < 80:
    print("Calificación: C")
elif 60 <= calificacion < 70:
    print("Calificación: D")
elif 0 <= calificacion < 60:
    print("Calificación: F")
else:
    print("Calificación no válida.")

print("-" * 30)

# Ejercicio 11: Evaluar valor respecto a cero
valor = float(input("Ingresa un valor: "))
if valor > 0:
    print("El valor es positivo.")
elif valor < 0:
    print("El valor es negativo.")
else:
    print("El valor es cero.")

print("-" * 30)

# Ejercicio 12: Clasificación simple de edad usando 19
edad_clasif = int(input("Ingresa una edad para clasificar: "))
if edad_clasif < 19:
    print("Eres menor de edad.")
elif edad_clasif <= 65:
    print("Eres mayor de edad.")
else:
    print("Eres un adulto mayor.")

print("-" * 30)
