#Aprendiendo ciclos for

for x in range(3):
    print("Jairo: "+str(x))

#Recorriendo lista
colores=["Azul","Blanco","Rojo","Morado"]
for i in colores:
    print(i)
#Imprimiendo rango de valores
for x in range(5,10):
    print(x)
print("XXXXXXXXXXXXXXXXXXXXXXX")
#Imprimiendo en intervalos
for x in range(5,10,2):
    print(x)
#Detener el ciclo cuando se llegue aun numero determinado
print("XXXXXXXXXXXXXXXXXXXXXXX")
for num in range(0,100,2):
    if(num>=15):
        break
    print(num)
#Usando el continue en ciclo for
for num in range(20):
    if(num==5 or num==9):
        continue
    print(num)
