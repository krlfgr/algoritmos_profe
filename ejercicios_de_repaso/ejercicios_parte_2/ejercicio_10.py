'''Ejercicio 2.10
Cree una tupla llamada ventas que considere
en la primera posición el nombre de un
producto y su precio. Para el ejemplo puede
considerar leche como el nombre y su precio
5. Utilice el método index para consultar el
índice correspondiente al precio. Ahora en
otra instrucción y utilizando el índice intente
reemplazar el elemento asignándole un
nuevo valor 8. ¿Qué interpreta del error que
sale al ejecutar la instrucción?'''

ventas=("Leche", 5)
indice=ventas.index(5)
print(indice)

ventas[indice] = 8
print(ventas)

'''el error que aparece en consola es: TypeError: 'tuple' object does not support item assignment
esto debido a que  las tuplas son inmutables: no se pueden cambiar, ni agregar, ni eliminar elementos una vez creadas.'''
