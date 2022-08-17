num1=0
num2=0
num3=0
print("Digite los tres numeros")
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3 and num2>num3:
    print("Resultados",num1,num2,num3)
elif num2>num1 and num2>num3 and num1>num3:
    print("Resultados",num2,num1,num3)
elif num3>num1 and num3>num2 and num1>num2:
    print("Resultados",num3,num1,num2)
elif num1>num2 and num1>num3 and num3>num2:
    print("Resultados",num1,num3,num2)
elif num2>num1 and num2>num3 and num3>num1:
    print("Resultados",num2,num3,num1)
elif num3>num1 and num3>num2 and num2>num1:
    print("Resultados",num3,num2,num178)