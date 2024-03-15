#Ex3. Tarea 11
def filtrar(lista, c):
    f =list(filter(lambda x: x[0]==c.lower or x[0]==c.upper(), lista))
    print("De la lista {}, las palabras que comienzan por {} son: {}".format(lista, c, f))

#Programa Principal
lista = ["Clara","María","Sebas","Cristobal","Zack","Carrasco"]
c = "c"
filtrar(lista, c)


