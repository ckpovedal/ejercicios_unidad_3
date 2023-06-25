import numpy as np
import random

#Array con for
#matriz = np.array([[0,1,2],[3,4,5]])
#for f in range (2):
#    for c in range (3):
#        print(matriz[f][c])


#Listas sin for
#lista = [[1,2,3],[4,5,6]]
#matriz = np.array(lista)
#print(matriz)

#Mostrar posicion de array con for
#matriz = np.array([[0,1,2],[3,4,5]])
#for f in range (2):
#    for c in range (3):
#        print(matriz[f][c])
#print("")
#print(matriz[1,2])

#Mostrar posicion como lista
#lista = [[1,2,3],[4,5,6]]
#matriz = np.array(lista)
#print(matriz[0][1])

#formas de mostrar posicion como lista
#lista = [[1,2,3],[4,5,6]]
#matriz = np.array(lista)
#print(matriz[1,1]) #mostrar posicion determinada
#print(matriz[:,2]) #mostrar solo columanda
#print(matriz[0,:]) #mostrar solo fila
#print(matriz[0,: :-1]) #mostrar columna en reverso

#matriz con ceros
#matriz = np.zeros((3,3))
#print(matriz)

#matriz con unos
#matriz = np.ones((3,3))
#print(matriz)

#matriz con diagonal principal con 1
#matriz = np.diag([4,5,10]) #se puede colocar el número que uno quiere
#print(matriz)

#Sumar todos los elementos
#lista = [[1,2,3],[4,5,6]]
#matriz = np.array(lista)
#print(matriz.sum())

#sumar elementos por fila
#lista = [[1,2,3],[4,5,6]]
#matriz = np.array(lista)
#print("Suma elementos fila 0: ", matriz[0,:].sum())
#print("Suma elementos fila 1: ", matriz[1,:].sum())

#
#matriz = np.array([[0,1,2],[3,4,5]])
#print(matriz.ndim) #indica dimensiones del array
#print(matriz.shape) #indica dimension del array y tamaño
#print(matriz.size) #indica cantidad de número es array

#concatenacion de arrays
#m1 = np.array([[1,2,3],[4,5,6]])
#m2 = np.array([[10,20,30],[40,50,60]])
#print(np.concatenate((m1,m2), axis=0))

#Ejercicio de Matriz con numeros aleatorios
matriz = np.random.randint(0,101, size=(3,3))
print(matriz)

#Promedio de elementos
print(matriz.mean())

#Suma de los elementos
print(matriz.sum())

#Mostrar elemento mayor
print(matriz.max())

#Mostral elemento menor
print(matriz.min())

#Diagonal principal
diag_prin = np.diag(matriz)
print(diag_prin)

#Ejercicio de Matriz con 0
matrizcero = np.zeros((3,3))
np.fill_diagonal(matrizcero, [1,2,3])
print(matrizcero)