#Ex9 Tarea 11
def pot(p):
    r = [x**p for x in range(1, 10)]
    print("Las potencias elevadas a {} de los 10 primeros números es {}".format(p,r))
#Programa Principal
p = int(input("Introduce un numero al qual voleu elevar la resta: "))
pot(p)