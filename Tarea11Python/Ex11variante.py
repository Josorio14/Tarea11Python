#Ex11. Tarea 11
def imprimir_fichero(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def añadir_fichero(m,lista):
    with open(m,"a+") as f:
        for e in lista:
            f.write(e+"\n")

#Programa Principal
fichero = "/home/cicles/AO/Python/Tarea11Python/Exer11.txt"
lista = ["Jordi, Claudia, Paula, Anas, Sebas, Clara"] 
añadir_fichero(fichero,lista)
imprimir_fichero(fichero)