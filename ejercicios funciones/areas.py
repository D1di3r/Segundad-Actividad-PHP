from cmath import pi
from multiprocessing.heap import Arena


def calarcu(lado):
    area=lado**2
    return area
def calarre(base,altura):
    area=base*altura
    return area
def calartri(base,altura):
    area=(base*altura)/2
    return area
def calarcir(radio):
    area=pi*(radio*radio)
    return area
def calarom(dia,dia1):
    area=(dia*dia1)/2
    return area
def calatra(basem,basemay,alturatra):
    area=((basemay+basem)*alturatra)/2
    return area

print("Digite un numero para calcular una figura")
print("1 para cuadrado, 2 para rectangulo, 3 para triangulo, 4 para circulo, 5 para rombo y 6 para trapecio")
num=int(input())
if num==1:
    ladoc=int(input("Digite El Lado del cuadrado"))
    areac= calarcu(ladoc)
    print("El area es: ",areac)
    
elif num==2:
    baser=int(input("Digite la base del rectangulo"))
    alturar=int(input("Digite la altura del rectangulo"))
    arear=calarre(baser,alturar)
    print("El area es:" ,arear)
elif num==3:
      baser=int(input("Digite la base del triangulo"))
      alturar=int(input("Digite la altura del triangulo"))
      arear=calartri(baser,alturar)
      print("El area es:" ,arear)
elif num==4:
   radioc=int(input("Digite el radio del circulo"))
   areacir= calarcir(radioc)
   print("El area es: ",areacir)
elif num==5:
    dias=int(input("Digite la primera diagonal del rombo (horizontal o vertical)"))
    dia2=int(input("Digite la segunda diagonal del rombo(horizontal o vertical)"))
    arearo=calarom(dias,dia2)
    print("El area es:" ,arearo)
elif num==6:
   
    baseme=int(input("Digite la base menor del trapecio"))
    basema=int(input("Digite la base mayor del trapecio"))
    alturatras=int(input("Digite la altura del trapecio"))
    areatra=calatra(baseme,basema,alturatras)
    print("El area es " ,areatra)
else:
    print("No deberias estar aqui")

    