'''Ejercicio 1.4
Escriba un programa que capture del usuario dos
valores a y b en dos inputs sucesivos. Pida al
usuario desde la función input que los valores a
ingresar deben contener al menos un número
decimal. Al ejecutar, el programa debe realizar la
multiplicación entre los dos valores y entregar la
respuesta en un formatted string que contenga
una variable llamada resultado y el texto de su
preferencia.'''

a=float(input("Ingrese el primer valor. Debe tener al menos un decimal: "))
b=float(input("Ingrese el segundo valor. Debe tener al menos un decimal: "))

#formatted string es una forma de insertar valores dentro de una cadena de texto de manera sencilla y legible.
resultado=(a*b)
print(f"El resultado de la multiplicacion entre {a} y {b} es {resultado}")