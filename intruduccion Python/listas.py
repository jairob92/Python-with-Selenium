lenguajes=["Php","Java","Phython"]
print(lenguajes)
#imprimir el primer valor
print("primer valor de la lista: "+lenguajes[0])
#imprimir el tercer valor
print("tercer valor de la lista: "+lenguajes[2])
lenguajes[1]="JavaScript"
#imprimir valor actualizado en la segunda posicion
print("Segundo valor de la lista "+lenguajes[1])
print(lenguajes)
#agregando nuevo lenguaje
lenguajes.append("Kotlin")
print(lenguajes)
#eliminando nuevo registro
lenguajes.remove("Kotlin")
print(lenguajes)