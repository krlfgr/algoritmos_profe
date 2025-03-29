'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

#a=int(input("por favor ingrese un número: "))
#b=int(input("por favor ingrese un número: "))
#c=int(input("por favor ingrese un número: "))
#d=int(input("por favor ingrese un número: "))
#e=int(input("por favor ingrese un número: "))

# lista=[a,b,c,d,e]
# #print(lista)

# lista.reverse()
# #print(lista)

# #objeto.metodos(*)
# #funcion(objetos)

# suma=sum(lista) #sum es una función aplicada a la lista
#print(suma)


#opción 2
entrada=input("ingrese los números a listar: ")
print(entrada)
print(type(entrada))
lista=list(entrada)
print(lista)
lista.reverse()
print(lista)
suma=sum(lista)
print(suma)