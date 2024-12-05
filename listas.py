lista =[1,2,3,4,5,6,7,8,9]
print(lista)
print(len(lista)) #Esto funciona para saber cual es la longitud de este 

for i in range(len(lista)):
    print(lista[i])
    
lista =[1,2,3,4,5,6,7,8,9]
elemento = input("Agregar elementos a la lista\n")
lista.append(float(elemento))
print(lista)    

lista = [1, 2, 3]
lista.extend([4, 5, 6])  # lista ahora es [1, 2, 3, 4, 5, 6]

lista = [1, 2, 3]
lista.insert(1, 'nuevo')  # lista ahora es [1, 'nuevo', 2, 3]

lista = [1, 2, 3, 2]
lista.remove(2)  # lista ahora es [1, 3, 2]

lista = [1, 2, 3]
elemento = lista.pop()  # elemento es 3, lista ahora es [1, 2]


lista = [3, 1, 2]
lista.sort()  # lista ahora es [1, 2, 3]

