'''Ejercicio 2.7
Utilizando la lista creada en el punto anterior
aplique el método que le permita eliminar la letra c
que se encuentra en la posición 3. Confirme que el
método utilizado devuelva la letra eliminada y que al
llamar nuevamente la lista el elemento no se
encuentre en la posición indicada.'''

lista=["a","b","c","d","e"]
elemento_eliminado=lista.pop(2) # Elimina y guarda el valor
print(elemento_eliminado)
print(lista)