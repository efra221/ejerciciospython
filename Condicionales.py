# x = 10

# if x > 18:
#     print("Mayor que 10")
# elif x == 10:
#     print("Igual a 10")
# else:
#     print("Menor que 10")
    
    
edad= 60

if edad >= 18:
    print("Mayor de edad")
elif edad >= 60:
    print("Adulto Mayor")
else:
    print("Menor de edad")
 
    
# Switch 

opciones = {
    1: "Opción 1",
    2: "Opción 2",
    3: "Opción 3"
}
seleccion = 3
resultado = opciones.get(seleccion, "Opción no válida")
print(resultado)

# Switch en Python con match
# Ejemplo: Días de la semana
def dia_de_la_semana(dia):
    match dia:
        case "lunes":
            return "Inicio de la semana laboral."
        case "viernes":
            return "¡Es viernes, casi fin de semana!"
        case "sábado" | "domingo":
            return "Fin de semana."
        case _:
            return "Día no válido."
        
# Uso del switch
print(dia_de_la_semana("lunes"))   # Salida: Inicio de la semana laboral.
print(dia_de_la_semana("sábado")) # Salida: Fin de semana.

x= 2
print("Mayor que 10") if x > 10 else print("Menor o igual a 10")