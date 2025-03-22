'''
TIPOS DE DATOS
<class 'int'>: Identifica que la variable es un entero
<class 'float'>: Identifica que la variable es un número decimal
<class 'str'>: Identifica que la variable es una cadena de texto
<class 'bool'>: Identifica que la variable es un valor True o False (boolean)
'''

x=True #True y False son palabras reservadas del lenguaje
#print(type(x))

autor='andres'
#print(type(autor))

carro="This is Andrews' car: "
modelo='1999'
#print(carro + modelo) #el simbolo + permite concatenar textos en Python


'''
TIPOS DE ESTRUCTURAS DE DATOS Y MÉTODOS
1. Conjuntos +
2. Tuplas ++
3. Listas   +++
4. Diccionarios   +++
'''

#Uso de conjuntos
'''
Los sets o conjuntos son estructuras especiales que nos ayudan a almacener
un grupo de elementos. Cuando el orden de los elementos no es relevante
podemos utilizar sets en Python.
Además esta estructura no permite elementos duplicados
cómo se definen: {, , , , ,}
<class 'set'>
'''
set1={"a", "b", 'c', 'd'}
#print(type(set1))

set2={"e", 'f', "g"}

#métodos para el tratamiento de conjuntos
set1.union()
# Unión de conjunto

#print(set1.union(set2))

set3={"a", "b", "c", "c", "d", "d"}
#print(set3)
set4=set3.union(set1)
#print(set4) #a,b,c,d

#Intersección de conjuntos con python
set5={"f", "w", "a", "b"}
#print(set5)
#print(set5.intersection(set1))

set5.remove("w")
#print(set5)

set4.add("a")
#print(set4)

#print(set4.issuperset(set5))
set4.issuperset(set5)

set6={"andres", 5, True}
set7={"andres", 5, True, "daniel"}
# print(set6.issuperset(set7)) # False
# print(set7.issuperset(set6)) # True

# print(set6.issubset(set7)) # True
# #print(set7.issubset(set6)) # False

'''
Uso de Tuplas
Son estructuras de datos rigidas, que no permiten muchos métodos
se usan cuando queremos resguardar la información (inmutable)
cómo se definen: (, , , , ,)
si permiten valores duplicados
<class 'tuple'>
'''
tupla1=(1,1,1,1,1,1,2,3,4,5)
 #      0,1,2,3,4,5,6,7,8,9
#print(type(tupla1))

#Métodos
#count
conteo=tupla1.count(1)
#print(conteo)

#index
indice=tupla1.index(5)
#print(indice)

'''
PYTHON ES UN LENGUAJE INDEXADO EN CERO
Siempre el primer elemento en una estructura de datos tiene 
el indice 0, en otras palabras, la posición inicial siempre es 0
indice <===> posición
'''

'''
USO DE LISTAS
Las listas en Python son estructuras de datos que almacenan 
elementos de manera ordenada y mutable. 
Son un tipo de dato nativo del lenguaje de programación Python. 
cómo se definen: [, , , , ,]
si permiten valores duplicados
<class 'list'>
pueden contener cualquier tipo de dato, 
número, letras, o incluso otras listas
'''

lista1=[8,9,7,5,4,10]
#print(type(lista1))


#print(type(lista2)) # <class 'list'>


#Métodos
#count
#print(lista1.count(14))

#reverse
lista3=lista1.reverse() #investigar
#print(lista3)
lista1.reverse()
#print(lista1)
lista1.append(20)
#print(lista1)

lista1.remove(7) 
print(lista1)

#Investigar reverse , sort

#Acceder a los elementos de la lista
lista2=[["jhon", "alejandro", "lewin",],["Isabel", "Juan", "Daniel"]]
print(lista2[0][1])

print("------")
#INVESTIGACIÓN
#reverse
lista1 = [8, 9, 7, 5, 4, 10]
lista1.reverse()  # Modifica lista1 en su lugar
print("Salida del método reverse ")
print(lista1)  # Ahora lista1 está invertida
# 
#Salida del método reverse
#[10, 4, 5, 7, 9, 8]
lista1 = [8, 9, 7, 5, 4, 10]
listad= list(reversed(lista1))  # Convierte el iterador en una lista nueva
print("esta es la lista d", listad)


#sort
lista2  = [8, 9, 7, 5, 4, 10]
lista2.sort() #en orden ascendente es por defecto
print("salida del método sort")
print(lista2)
#salida del método sort
#[4, 5, 7, 8, 9, 10]
lista2.sort(reverse=True)
listac=lista2.sort(reverse=True)
print("salida del método sort con reverse True")
print(lista2)

#salida del método sort con reverse True -->orden descendente
#[10, 9, 8, 7, 5, 4]
lista2.sort()

#FIRMA DEL MÉTODO SORT
#list.sort(*, key: None = None, reverse: bool = False) -> None
'''
* → Indica que los parámetros después de este deben pasarse por nombre 
(es decir, key= y reverse= deben especificarse explícitamente).

key: None = None → Parámetro opcional que permite definir una función personalizada 
para ordenar los elementos.

reverse: bool = False → Si es True, ordena en orden descendente; si es False,
ordena en ascendente (por defecto).

-> None → Indica que el método no devuelve nada (None), 
sino que modifica la lista en su lugar (in-place).
'''
