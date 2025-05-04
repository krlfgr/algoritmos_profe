'''Ejercicio 2.12
Defina un conjunto vacío denominado figuras. A
continuación, utilice un método para que el
conjunto contenga los nombres de tres figuras
geométricas, por ejemplo: circulo, cuadrado,
rectángulo. Aplique un método que permita
agregar un nuevo elemento utilizando
exactamente uno de los nombres ya definidos.
Consulte el estado actual del conjunto figuras
¿qué interpreta del resultado?'''

figuras=set()
figuras.update({"circulo", "cuadrado", "triangulo"})
print(figuras)
figuras.add("circulo")
print(figuras) # no es posible agregar un nombre ya existente. En los sets no se permiten duplicados.