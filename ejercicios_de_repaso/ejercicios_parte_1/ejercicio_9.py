'''Ejercicio 1.9
Compruebe mediante el operador de identidad
correspondiente si la letra w se encuentra en la
expresión “Python es un lenguaje de programación
muy popular”. Utilice un input para consultar lo
mismo y comprobar según la entrada que dé el
usuario.'''

letra=(input("Ingrese la letra que quiere buscar: "))
expresion="Python es un lenguaje de programación muy popular"

resultado=letra in expresion
print(resultado)