from functools import total_ordering


precio=0
numllantas=0

print("Digite el numero de llantas")
numllantas=int(input())
if numllantas<=5:
    precio=240000
    total=numllantas*precio
    print("El total es:",total,"Precio de las llantas",precio)
elif numllantas==6 or numllantas==7:
    precio=221000
    total=numllantas*precio
    print("El total es:",total,"Precio de las llantas",precio)
elif numllantas>7:
    precio=180000
    total=numllantas*precio
    print("El total es:",total,"Precio de las llantas",precio)
else:
    print("No deberias estar aqui")