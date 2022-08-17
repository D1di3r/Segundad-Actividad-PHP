preciota=0
tamal=0
desc=0

print("Bienvenido a nuestro local")
print("¿Cuantos tamales va a comprar?")
tamal=int(input())
print("¿Precio del tamal?")
preciota=int(input())
if tamal<=5:
    print("No hay descuento")
elif tamal>5 and tamal<10:
    desc=0.05
    preciota=preciota-preciota*desc
    total=tamal*preciota
    print("Se le hace un decuento del 5%")
    print("Debe pagar ", total)
elif tamal>=10:
    desc=0.08
    preciota=preciota-preciota*desc
    total=tamal*preciota
    print("Se le hace un decuento del 8%")
    print("Debe pagar ", total)
else:
    print("No")
