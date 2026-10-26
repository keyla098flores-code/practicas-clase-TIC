#prorama bonos_empleado
#requisitos
nombre=(input("dime tu nombre"))
pago=float(input("dime tu pagp por hora"))
horas=float(input("dime cuantas horas trabajas al mes"))
#calculra sueldo
sueldo=pago * horas
print("tu sueldo es ",sueldo)
print(f"tu sueldo es {sueldo}")
#condicionales
if sueldo>=100 and sueldo<=300:
    bono=sueldo + 500
    print(f"tu pago final es {bono}")
elif sueldo>300 and sueldo<=1500:
    bono=sueldo +1700
    print(f"tu pago final es {bono}")
elif sueldo>1500 and sueldo<=3000:
    bono=sueldo + 3500
    print(f"tu pago final es {bono}")
elif sueldo>3000 and sueldo<8000:
    bono=sueldo + 8500
    print(f"tu pago final{bono}")
elif sueldo>8000:
    bono=sueldo + 10000
else:
    print("no valido")
