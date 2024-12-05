#Definicion de funcion

def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()  # Imprime "¡Hola, mundo!"


# Funciones para parametros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

usuario = input("Ingrese su nombre: ")

# Llamar a la función con un argumento

saludar(usuario)  # Imprime "¡Hola, (usuario)!"

# Funciones con retorno

def sumar(a, b):
    return a + b

num1 = int(input("Ingrese el primer numero a sumar: "))
num2 = int(input("Ingrese el Segundo numero a sumar: "))


resultado = sumar(num1, num2)

print(resultado)  # Imprime 8

suma = lambda x, y: x + y

resultado = suma(4, 7)
print(resultado)  # Imprime 11