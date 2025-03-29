'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''
estudiantes={
    "diana":4.8,
    "luis":3.5,
    "jose":4.6
}
consulta=input("por favor ingrese el estudiante a consultar: ")
print(estudiantes.get(consulta, "el estudiante no está"))
print(estudiantes[consulta])
