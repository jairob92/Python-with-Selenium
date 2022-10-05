#creando mi primera funcion

def saludo():
    print("Imprimiendo desde una funcion")
    a=10;
    b=20;
    c=a+b
    print(a)
    print(b)
    print("imprimiendo la suma de {} +{} es: {}".format(a,b,c))

saludo()

#Funciones com paramentros

def suma(a,b):
    print("El valor de a es"+str(a))
    print("El valor de b es" + str(b))
    c=a+b
    print("El resultado de {} + {} es :{}".format(a,b,c))
suma(4,2)

#Funcion con *args

def funcion(*args):
    resultado=0
    for n in args:
        resultado=resultado+n

    print("El resultadoes:"+str(resultado))

funcion(2,3)