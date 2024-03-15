from functools import reduce
def pasar_numero(lista):
    a = list(map(lambda a: str(a), lista))
    b = reduce(lambda x,y:x+y,a)
    print(b)
#Programa principal
a =[1, 3, 5, 6]
pasar_numero(a)