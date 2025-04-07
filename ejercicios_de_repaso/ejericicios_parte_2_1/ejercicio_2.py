'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''

x=str(input("Ingrese una palabra: "))
frase=("Python es un lenguaje de programacion poderoso")

resultado=x in frase
print(resultado)