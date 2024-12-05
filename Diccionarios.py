# Solución
alumno = {
    "nombre": "Juan",
    "edad": 20,
    "curso": "Matemáticas"
}

# Imprimir el diccionario
#print(alumno)

#print(alumno["nombre"])  # Imprime: Juan

#agregar un elemento al diccionario
alumno["nota"] = 8.5
print(alumno)

# Eliminar un elemento del diccionario
del alumno["curso"]
print(alumno)


# Recorre el diccionario
for clave, valor in alumno.items():
    print(clave, ":", valor)
    
#Diccionario anidado
clase = {
    "alumno1": {"nombre": "Ana", "edad": 21, "nota": 9.0},
    "alumno2": {"nombre": "Carlos", "edad": 22, "nota": 7.5}
}

# Imprimir el diccionario completo
print(clase)        

# Modificar un Valor en Diccionario Anidado
clase["alumno1"]["nota"] = 9.5
print(clase["alumno1"])