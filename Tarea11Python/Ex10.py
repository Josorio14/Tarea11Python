#Ex10. Tarea 11
def div(a,b):
    try:
        c = a//b 
        print("La división de {} entre {} es: {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segundo parametro no puede ser cero")

#Programa principal 
a= int(input("Escribe el numerador: "))
b = int(input("Escribe el denominador: "))
div(a,b)