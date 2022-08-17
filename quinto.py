from cmath import pi


num=0
areac=0
arear=0
areat=0
areacir=0
arearom=0
areatra=0

print("Digite un numero para calcular una figura")
print("1 para cuadrado, 2 para rectangulo, 3 para triangulo, 4 para circulo, 5 para rombo y 6 para trapecio")
num=int(input())
if num==1:
    print("Digite los numeros para calcular el area")
    ladoc=int(input())
    areac=ladoc*ladoc
    print("El area es " ,areac)
elif num==2:
    print("Digite los numeros para calcular el area del rectangulo (base y altura)")
    baser=int(input())
    alturar=int(input())
    arear=baser*alturar
    print("El area es " ,arear)
elif num==3:
    print("Digite los numeros para calcular el area del triangulo (base y altura)")
    baset=int(input())
    alturat=int(input())
    areat=(baset*alturat)/2
    print("El area es " ,areat)
elif num==4:
    print("Digite el radio para calcular el area del circulo")
    radio=int(input())
    areacir=pi*(radio*radio)
    print("El area es " ,areacir)
elif num==5:
    print("Digite los datos para calcular el area del rombo ")
    diagonal=int(input())
    diagonal2=int(input())
    arearom=(diagonal2*diagonal)/2
    print("El area es " ,arearom)
elif num==6:
    print("Digite los datos para calcular el area del trapecio (base menor, base mayor y la altura) ")
    baseme=int(input())
    basema=int(input())
    alturatra=int(input())
    areatra=((basema+baseme)*alturatra)/2
    print("El area es " ,areatra)
else:
    print("No deberias estar aqui")
