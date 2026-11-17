#lista:busqueda
nombres=["angel","karla","luis","mateo","maria","luis","karla"]
print(f"los nombres que se tienen son :{nombres}")
nombreBuscar=input("¿que nombre deas buscar:")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("encontrado en la posicion:",i)
        i=i+1
if encontrado == True:
    print("nombre encontrado")
    print("aparece",contador,"veces")
    if contador > 1:
     nombres.remove(nombreBuscar)
else:
    print("nombre no encontrado")
print(nombres)
