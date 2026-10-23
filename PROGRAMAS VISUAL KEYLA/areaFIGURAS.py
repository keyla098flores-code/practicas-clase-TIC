#programa para calcular areas
#Area cuadrado; lado x lado 
lado=float(input("ingresa lado"))
areaCuadrado=lado*lado
print("El area es ", areaCuadrado)
print(f"El area es {areaCuadrado}")
#Area triangulo (base x altura)/2
base=float(input("ingresa la base"))
altura=float(input("ingrasa la aLtura"))
areaTriangulo=base*altura/2
print("El area es ",areaTriangulo)
print(f"El area es{areaTriangulo}")
#Area de un trapecio(base mayor + base menor X ALTURA)/2
basemayor=float(input("ingresa base mayor"))
basemenor=float(input("ingresa base menor"))
altura=float(input ("ingre altura"))
areaTrapecio=basemayor + basemenor * altura / 2
print("El area es", areaTrapecio)
print(f"El area es{areaTrapecio}")
#Area de circulo (3.14 x radio *radio)
radio=float(input(" escribe el valor del radio "))
areaCirculo=3.14*radio*radio
print("El area es" ,areaCirculo)
print(f"El area es ", {areaCirculo})
#area de pentagono (perimetro x apotema)/2
perimetro=float(input("ingresa el valor del perimetro"))
apotema=float(input("ingresa el valor del apotema"))
areaPentagono=perimetro*apotema/2
print("El area de es",areaPentagono)
print(f"El area es {areaPentagono}")