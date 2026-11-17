#Lista:de numeros y multiplicacionh
numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("ingresa un numero:"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿por cuantos deseas multiplicar?:"))
for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)
print("numeros originales:",numeros)
print("resultados:",resultados)
numbusc=int(input("escribe el numero que quieres buscar en la lista:"))
if numbusc in resultados:
    print("el numero si esta en la lista")