'''Ejercicio 2.8
Cree una lista con los números del 1 al 10
considerando el orden de su preferencia.
Llame a la lista valores. Aplique un método
que le permita ordenar los valores desde el
mayor al menor. Si ahora utiliza la función
sorted sobre la lista, ¿qué diferencia
encuentra?.'''

valores=[2,1,5,9,3,7,6,4,8,10] 
valores.sort(reverse=True) # .sort() => ordena la lista modificando la lista original
print(valores)

#usando .sorted()
valores=[2,1,5,9,3,7,6,4,8,10] 
valores_ordenados= sorted(valores, reverse=True) # .sorted() => devuelve una lista nueva ordenada
print(valores_ordenados)