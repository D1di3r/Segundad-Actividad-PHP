edad=0
genero=0
print("Digite la edad")
edad=int(input())
print("Digite el genero (1 para mujer 2 para hombre)")
genero=int(input())
if genero==1:
    pulsaciones=(220-edad)/10
    print("Sus pulsaciones son:",pulsaciones)
elif genero==2:
    pulsaciones=(210-edad)/10
    print("Sus pulsaciones son:",pulsaciones)
else:
    print("Usa 1 o 2")