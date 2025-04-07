
#Ejercicio 1.5
'''
Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.
'''
dividendo=int(input("Ingrese el primer número "))
divisor=int(input("Ingrese el segundo número "))


#Calculos
cociente=dividendo/divisor
residuo=dividendo%divisor

print(f"La comprobación de la división es: {divisor} por {cociente} más {residuo} es igual a {dividendo}")