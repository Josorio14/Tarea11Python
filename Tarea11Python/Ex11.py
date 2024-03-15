#Ex11. Tarea 11
def imprimir_fichero(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

#Programa Principal
fichero = "/home/cicles/AO/Python/Tarea11Python/Exer11.txt"
imprimir_fichero(fichero)

