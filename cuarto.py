num1=0
num2=0
num3=0
num4=0
num5=0
promedio=0
print("Digite las notas")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
promedio=(num1+num2+num3+num4+num5)/5
if promedio>=3.0:
    print("Aprobo con" ,promedio)
elif promedio<3.0:
    print("Desaprobo con ",promedio)
else:
    print("xd")