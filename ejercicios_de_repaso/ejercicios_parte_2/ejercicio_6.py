'''Ejercicio 2.6
Cree un programa que defina una lista con las
primeras cinco letras del alfabeto en minúscula.
Posterior a la creación de la lista, aplique un método
para insertar en la posición 2 la letra a. Ahora,
aplique un método para contar el número de veces
que la letra a se encuentra en la lista creada.'''

lista=["a","b","c","d","e"]
lista.insert(2,"a")     # .insert(posicion, elemento)
print(lista)
print(lista.count("a"))