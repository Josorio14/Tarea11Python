#Ex5 Tarea 11
def crear_diccionario(lista):
    dic = {}
    for i, e in enumerate(lista):
        dic[e]=i
    print("De la lista {} hemos creado el dicionario {}".format(lista,dic))

#Programa principal
lista =["Coche","Casa","Barco","Amor","Sebas","Clara","Perro"]
crear_diccionario(lista)