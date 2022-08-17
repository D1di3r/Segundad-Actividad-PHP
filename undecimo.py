peso=0
tallam=0
imc=0

print("Digite el peso y la talla")
peso=int(input())
tallam=float(input())
imc=peso/(tallam*tallam)
if imc<20:
    print("Estas desnutrido" ,imc)
elif imc>=20 and imc<25:
    print("Normal",imc)
elif imc>=25 and imc<30:
    print("Sobrepeso",imc)
elif imc>=30 and imc<35:
    print("obesidad grado 1",imc)
elif imc>=35 and imc<=40:
    print("Obesidad grado 2",imc)
elif imc>40:
    print("Obesidad grado 3",imc)
else:
    print("XD")