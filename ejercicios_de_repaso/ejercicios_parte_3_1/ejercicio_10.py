'''Ejercicio 10: Clasificación de Edades

Problema:
Solicitar 1 edad y clasificarlas en menores de edad (0-17), adultos (18-64) y adultos mayores (65+)'''

edad=float(input("Por favor ingrese la edad: "))

#Version 1
if edad>=0 and edad<=17:
    print("Es menor de edad")
elif edad>17 and edad<=64:
    print("Es adulto")
elif edad>64:  #elif siempre espera una condicion
    print("Es adulto mayor")

#Version 2
if edad in range(0,18):
    print("Es menor de edad")
elif edad in range(18,65):
    print("Es adulto")
else:
    print("Es adulto mayor")

#Version 3
match edad:
    case range(0,18):
        print("es menor de edad")
    case range(18,65):
        print("es adulto")
    case range(65,120):
        print("Es adulto mayor")