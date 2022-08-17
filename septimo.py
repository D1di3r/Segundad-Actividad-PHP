from ast import Num


num=0

print ("¿Como desea pagar?")
print ("Si escribe uno es para pagar con efectivo valores menos o iguales a 150000")
print ("Si desea pagar con el celular escriba 2 valores de 150k a 300k")
print ("Si desea pagar con tarjeta escriba 3 valores de 300k a 600k")
num=int(input())
if num==1:
    print("Ha decidido pagar con efectivo gracias por su compra vuelva pronto")
elif num==2:
    print("Ha decidido pagar con dinero digital (celular) gracias por su compra vuelva pronto")
elif num==3:
    print("Ha decidido pagar con tarjeta gracias por su compra")