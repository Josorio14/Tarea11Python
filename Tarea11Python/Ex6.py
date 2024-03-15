#Ex6 Tarea 11
def coincidencia(lista):
    l = []
    for i, e in enumerate (lista):
        if e == i:
            l.append(e)
    print("Los elementos de la lista {} \n que coinciden en su posición son: \n {}".format(lista,l))

#Programa principal
l = [3, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1] 
coincidencia(l)

