'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
a=float(input("ingrese el 1er elemento"))
b=float(input("ingrese el 2do elemento"))
conjunto1={a,b}

c=float(input("ingrese el 1er elemento"))
d=float(input("ingrese el 2do elemento"))
conjunto2={c,d}
print("el conjunto 1 es: ", conjunto1)
print(f"el conjunto 2 es: {conjunto2} ")

union=conjunto1.union(conjunto2)
print(union)
union_2= conjunto1 | conjunto2 #Ó en conjuntos suma elementos
print(union_2)
inteserccion=conjunto1.intersection(conjunto2)
print(inteserccion)
interseccion_2=conjunto1 & conjunto2 #Y en conjuntos encuentra elementos comunes
print(interseccion_2)