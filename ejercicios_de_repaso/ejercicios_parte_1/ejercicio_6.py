'''Ejercicio 1.6
Teniendo en cuenta el ejercicio anterior calcule el
residuo con el símbolo de módulo % y entregue la
comprobación con los valores resultantes de dividir
dos números entregados por el usuario del
programa.'''

dividendo=int(input("Ingrese el primer número "))
divisor=int(input("Ingrese el segundo número "))


#Calculos
cociente=dividendo//divisor
residuo=dividendo%divisor

#Resultados
print(f"Resultado de la división: {dividendo} / {divisor} = {cociente}")
print(f"Residuo: {dividendo} % {divisor} = {residuo}")

#Comprobacion
print(f"Comprobación: {cociente} * {divisor} + {residuo} = {cociente * divisor + residuo}")
print(f"Valor original: {dividendo}")
