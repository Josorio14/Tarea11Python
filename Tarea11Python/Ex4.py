#Ex4. Tarea 11
def conectar(l,d,c):
    a = []
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
        print("La unión de las listas {} y {} es: {}".format(l,d,a))

#Programa Principal
l = ["Super","Hiper","Mini","Maxi"]
d = ["Women","bole","Mouse","Boom"]
conectar(l,d,"-")
