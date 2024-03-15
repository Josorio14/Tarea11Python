#Ex7 Tarea 11
def Stringtolist(c):
    r = [x for x in c] #crea una lista con cada uno de los elementos 
    print("De la cadena {} hemos creado la lista {}".format(c,r))

#Programa principal
c = input("Introduce una palabra: ")
Stringtolist(c) 