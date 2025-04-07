'''
Ejercicio 1: Operadores Aritméticos

Problema: Escribe un programa que solicite al usuario dos números y 
realice las operaciones de suma, resta, multiplicación, división y módulo.

'''

x=float(input("Ingrese el valor del primer numero: "))
y=float(input("ingrese el valor del segundo numero: "))

a=(x+y)
b=(x-y)
c=(x*y)
d=(x/y)
e=(x%y)

print(f"El resultado de la suma entre {x} y {y} es de: {a}")
print(f"El resultado de la resta entre {x} y {y} es de: {b}")
print(f"El resultado de la multiplicacion entre {x} y {y} es de: {c}")
print(f"El resultado de la division entre {x} y {y} es de: {d}")
print(f"El resultado del modulo de la division entre {x} y {y} es de: {e}")