#Ex1. Tarea 11
def lenp(frase):
    r= frase.split(" ")
    l = list(map(len,r))
    print("La longitud de las palabras de la lista {} es: {}".format(frase,l))

#Programa principal
frase = input("Escribe una frase: ")
lenp(frase)