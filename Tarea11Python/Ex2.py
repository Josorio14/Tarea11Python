#Ex2. Tarea 11
from functools import reduce 
def Palabra_a_numero(lista):  
    a = list(map(lambda x: str(x), lista))
    b = reduce(lambda x,y: x+y, a)
    print("La lista  {} es el número {}".format(a,b))

#Programa Principal
l = [3,5,6,9,1]
Palabra_a_numero(l)  