'''clasificar los dias de la semana'''

dia=input("Por favor ingresar el dia de la semana: ").lower()

match dia:
    case "martes" | "miercoles" | "jueves" | "viernes":
        print("es dia laboral")
    case "lunes":
        print("es festivo")
    case "sabado" | "domingo":
        print("es fin de semana")
    case _:
        print("No es un dia de la semana")