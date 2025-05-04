'''Ejercicio 2.11
Con la tupla definida en el ejercicio anterior aplique
el método count para consultar cuántas veces 
aparece la letra “e” dentro de la tupla, de esta manera:
>>> ventas.count(“e”)
Interprete el resultado
Posteriormente indexe la tupla y consulte
cuántas veces aparece la letra “e” dentro del
primer elemento de la tulpa.
>>> ventas[0].count(“e”)
¿Qué diferencias encuentra en los dos
resultados?'''

ventas=("Leche", 5)

conteo=ventas.count("e") # cuenta cuantas veces aparece "e" dentro de la tupla ventas.
print(conteo) # como "e" no es un elemento completo de la tupla, el resultado va a ser 0

conteo1=ventas[0].count("e") # accede al primer elemento y luedo usa el metodo .count
print(conteo1) # cuenta cuantas veces aparece la letra "e" dentro de la palabra "leche"