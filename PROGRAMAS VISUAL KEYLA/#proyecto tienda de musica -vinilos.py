#proyecto tienda de musica -vinilos
print("bienvenido a la tirnda de vinilos karpe diem")
#diccionaros
vinilo1={
    "album": "fine line",
    "codigo" : 405,
    "artista": "harry styles",
    "precio" :  750,
    "stock" : 5
}
vinilo2={
    "album" : "thriller",
    "codigo" : 101,
    "artista" : "bruno mars",
    "precio" : 700,
    "stock" :  4
}
vinilo3={
    "album" :  "24kmagic",
    "codigo" : 302,
    "artista" : "bruno mars",
    "precio" : 700,
    "stock" :4
}
vinilo4={
    "album" : " A night at the opera",
    "codigo" :578,
    "artista" : "freddie mercury",
    "precio"  : 780,
    "stock"  : 6
}
vinilo=[vinilo1,vinilo2,vinilo3,vinilo4]
op=1
while op!=7:
print("------Tienda de vinilos----")
print("1.ingresa el codigo del vinilo")
print("2.buscar vinilo por codigo ")
print("3.modificar informacion de un vinilo")
print("4.comprar vinilo")
print("5.eliminar un vinilo")
print("6.mostrar los vinilos registrados")        
print("7.salir")
op=int(input("ingresa una opcion"))
if (op==1):
    print("--------AGREGAR UN VINILO------")
    codigo=int(input("ingresa el codigo del vinilo"))
    existe=False
    for v in vinilo["codigo"] == codigo:
        existe = True
        break
    if existe :
        print("Error: ese codigo ya esta registrado.")
    nuevo_vinilo={
        "nombre de el album":input("ingresa el nombre :"),
        "nombre del artista":int(input("ingresa el nombre .")),
        "precio" : float(input("ingresa el precio del album : ")),
        "codigo" : float(input("ingresael codigo del vinilo : ")),
        "stock" : float(input("ingresa la cantidad en stock : "))
    }
    vinilo.append(nuevo_vinilo)
    print("vinilo agregado")
elif (op==2):
    print("------VER VINILO POR CODIGO------")
    
elif (op==3):
    print("-------MODIFICAR LA INFORMACION DE UN VINILO---")
elif (op==4):

  
