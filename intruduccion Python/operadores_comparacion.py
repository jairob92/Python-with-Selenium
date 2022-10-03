#Comparadores logicos
a=10
b=9
c=5
print("a y b Son iguales: "+str(a==b))
print("a es menor que b: "+str(a<b))
print("a es mayor que b: "+str(a>b))
print("a es menor o igual que b: "+str(a<=b))
print("a es mayor o igual que b: "+str(a>=b))
print("a es diferente de b: "+str(a!=b))
#Comparado "AND"
print("Si a es menor que b y a es menor que c: "+str(a<b and a<c))
print("Si c es menor que b y c es menor que a: "+str(c<b and c<b))
#Comparando "OR"
print("Si a es menor que b o c es menor que b "+str(a<b or c<b))
print("Si a es mayor que b o b es igual que c "+str(a>b or b==c))
