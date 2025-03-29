'''
condicional "if then else"
"si se cumple una condición
entonces se realiza una operación
de lo contrario, se realiza otra operación (opcionalmente)"
'''

x = 100
y = 200
if x > y: #condición
    print("x es mayor que y") #operación

#uso del control if-else
#else: significa "de lo contrario"

w = 500
z = 2000
if w > z: #condición
    print("w es mayor que z") #operación
else:                         #de lo contrario
    print("w es menor que z") #operación

#uso del control if-elif-else
w = 500
z = 2000
if w > z: #condición 1
    print("w es mayor que z") #operación
elif w==100: #condición 2...
    print("el valor de w es 100")
elif w==500: #condición 3...
    print("el valor de w es 500")
else:                         #de lo contrario
    print("w es menor que z") #operación
'''
elif sirve para evaluar múltiples condiciones
'''
#uso de if anidados
# usuario=input("por favor ingrese su usuario: ")

# if usuario=="andres": #condicion 1 se cumple?
#     password=input("por favor ingrese su contraseña: ") #operación
#     if password=="1234": #condición 2 se cumple?
#         print("usuario puede acceder")
#     else:
#         print("La contraseña es incorrecta")
# else:
#     print("el usuario no existe")
    
usuario=input("por favor ingrese su usuario: ")
password=input("por favor ingrese su contraseña: ") #operación
#print(len(usuario))
#print(password.isnumeric())
if len(usuario)==5 and password.isnumeric(): #condicion 1 se cumple?
    print("usuario puede acceder")
else:
    print("el usuario o la contraseña no es válida")
