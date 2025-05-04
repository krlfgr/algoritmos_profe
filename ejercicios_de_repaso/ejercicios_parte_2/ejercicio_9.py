'''Ejercicio 2.9
Considere la creación de una nueva lista
llamada duplicada que sea una copia de la
lista valores. Posteriormente ejecute una
instrucción para que la copia quede
ordenada desde los valores más bajos a los
más altos.'''

valores=[2,1,5,9,3,7,6,4,8,10]
duplicada=valores.copy()
duplicada.sort()
print(duplicada)