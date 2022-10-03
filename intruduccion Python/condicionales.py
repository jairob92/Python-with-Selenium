#probando condicionales en python
print("Digite el valor de a")
a=input()
a=int(a)
print("Digite el valor de b")
b=input()
b=int(b)
if(a>b):
    print("{} es mayor que {}".format(str(a),str(b)))
elif(a==b):
    print("{} y {} son iguales".format(a,b))
elif(a!=b):
    print("{} es diferente de {}".format(a,b))
else:
    print("{} es menor que {}".format(str(b),str(a)))