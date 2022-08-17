
from ast import Num
from http.client import PRECONDITION_FAILED

num=0
precio=0
extras=4000
canextras=0
total=0


print("Digite el tamaño de la pizza")
print("1 para pequeña, 2 para mediana y 3 para grande")
num=int(input())
if num==1:
    precio=15000
    print("Digite la cantidad de ingredientes extra cada uno vale 4000")
    canextras=int(input())
    total=(extras*canextras)+precio
    print("El total es:",total)
elif num==2:
    precio=24000
    print("Digite la cantidad de ingredientes extra cada uno vale 4000")
    canextras=int(input())
    total=(extras*canextras)+precio
    print("El total es:",total)
elif num==3:
    precio=36000
    print("Digite la cantidad de ingredientes extra cada uno vale 4000")
    canextras=int(input())
    total=(extras*canextras)+precio
    print("El total es:",total)
else:
    print("Solo los tres numeros indicados")