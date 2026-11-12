def calcular_area(poligono):
    poligono = poligono.capitalize() # Comvierte "triangulo" a "Triangulo"

    if poligono == "Triangulo":
        base = float(input("Digite la base del triangulo: "))
        altura = float(input("Digite la altura del triangulo: "))
        return (base*altura) / 2
    elif poligono == "Cuadrado":
        lado = float(input("Digite el lado del cuadrado: "))
        return lado * lado
    elif poligono == "Rectangulo":
        lado_a = float(input("Digite el lado menor del rectangulo: "))
        lado_b = float(input("Digite el lado mayor del rectangulo: "))
        return lado_a * lado_b

area_t = calcular_area("Triangulo")
print(f"El area del triangulo es {area_t}")

area_r = calcular_area("Rectangulo")
print(f"El area del rectangulo es {area_r}")

area_c = calcular_area("Cuadrado")
print(f"El area del cuadrado es {area_c}")