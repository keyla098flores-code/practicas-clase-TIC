# programa que me indica como me fue
calif=float(input("Dame tu calif"))
if calif==10:
    print("Exelente!!!")
elif calif==9:
    print("Muy bien")
elif calif==8: 
    print("Bien")
elif calif==7:
    print("Puedes mejorar")
elif calif==6:
    print("ay mijooo")
else:
     print("chanclazoooo")

#programa que me indica si hace mucho calor
temp=float(input("dime la temperatura"))
if temp==40:
         print("Hace mucho calor")
elif temp>=30 and temp<40:
     print("Esta templadito")
elif temp>=20 and temp<30:
     print ("Esta fresco")
elif temp<20:
     print("Hace frio")
else:
     print("No valido")