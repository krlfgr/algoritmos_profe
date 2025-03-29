'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''
productos={
    "manzana":500,
    "pera":800,
    "limón":100
}
producto=input("Por favor ingrese el nombre del producto")
precio=float(input("Por favor ingrese el precio"))

productos[producto]=precio #forma de agregar clave y valor
#Nota: si la clave ya existe se actualiza el valor
print(productos)