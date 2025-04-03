'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''
a=(input("por favor ingrese una ciudad: "))
b=(input("por favor ingrese una ciudad: "))
c=(input("por favor ingrese una ciudad: "))
tupla=(a,b,c)
print(tupla[0])
print(tupla[-1])

# (0,1,2,3,4,...)

# (...,-3,-2,-1)
print(len(tupla[0]), len(b), len(c))
