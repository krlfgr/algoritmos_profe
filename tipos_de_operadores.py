
'''
Operadores aritméticos
'''

# Suma
# x=2+6
# print(x)


# Resta
y=8-2
# print(y)

# Multiplicación
# print(2*25)


#División
''' para python la división siempre retorna un float'''
divide=25/5
# print(divide)
# print(type(divide))

#División piso (floor)
'''
la división piso me devuelve el número entero más próximo
hacia abajo
'''
# print(10/3)
# print(10//3)

# print(4/3)
# print(4//3)

# print(14.5/3)
# print(14.5//3)

'''
Prueba realizar la división piso 8//-3 y 
compárala con la división tradicional 8/-3.
'''

#Módulo
w=20/3
y=20%3

# print(w)
# print(y)

# print(type(y))


#Potencia
# print(2**3)

'''
Operadores de comparación
Este tipo de operadores los usamos cuando deseamos comparar
expresiones o variables. Python evalúa si se cumple la
comparación y nos devuelve (retorna) un valor True o False
'''

#Es igual a
# print("x"=="X")

# print(3==3.0)
# print(3==3.0000000)
# print(3==3.000000000000000000000001)

# es diferente a
# print(4!=3)
# print(False != True)

#es mayor que
#>
# print(4>8)
#es menor que
#<

# es mayor o igual que , es menor o igual que
#>=
#<=

'''
Operadores de asignación
'''
x=20
x=20 + 1
# print(x)
#Incremento
# +=
# print(x++2)

#Decrecimiento
y=5
y=y-1
y-=1
print(y)


# Asigna multiplicación

# Asigna división

# Asigna módulo

#Asigna exponente


'''
Operadores lógicos
and: exige que todas las condiciones sean True para responder True, de lo contrario responde False
or: este operador solo necesita que alguna de las condiciones sea True para responder True
not
'''
x=4 #Defino el valor de la variable x
# x==4 #Preguntando si x es igual a 4
y=4
# print(x==4 and y==8)

#uso del operador or
print(x==100 or y==4)

#uso del operador no
'''
En el caso del operador not se valida si una variable es False o True. 
Si la variable existe en memoria tenemos un valor por defecto True.
'''
print(not x)

enunciado=False
print(not enunciado)

usuario_logueado=True
boton_logout=True
print(not usuario_logueado)