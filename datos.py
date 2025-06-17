# Ejemplo de declaración de variables y mostrar tipo, valor e ID

# Declaración de variables
edad = 19                 # int
estatura = 1.80           # float
nombre = "Carlos"         # str
es_estudiante = False     # bool

print("Edad:")
print("  Tipo:", type(edad))
print("  Valor:", edad)
print("  ID:", id(edad))

print("\nEstatura:")
print("  Tipo:", type(estatura))
print("  Valor:", estatura)
print("  ID:", id(estatura))

print("\nNombre:")
print("  Tipo:", type(nombre))
print("  Valor:", nombre)
print("  ID:", id(nombre))

print("\n¿Es estudiante?")
print("  Tipo:", type(es_estudiante))
print("  Valor:", es_estudiante)
print("  ID:", id(es_estudiante))

print("-" * 30)

# Ejemplo con enteros
x = 15
y = -4
z = 27
print("Números enteros:", x, y, z)

print("-" * 30)

# Suma de dos números ingresados por el usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
resultado = num1 + num2
print("La suma es:", resultado)
