def menu():
    op = 0
    while op< 1 or op >14:
        print("""
            \n
            Menu principal:
            1.Estructures condicionals, if
            2.Estructures condicionals, match
            3.Estructures iterativas, for e in b
            4.Estructures iterativas, for i in range(x)
            5.Estructures iteratives, for i,e in enumerate(a)
            6.Funcio amb paràmetres
            7.Funció lambda
            8.Funció list compehension
            9.Funció map
            10.Funció zip
            11.Funció filter
            12.Classes i Objectes
            13.Fitxers
            14.Sortir
            """)
        
        op = int(input("Introdueixi una opció: "))
        if op< 1 or op >14:
            print("Opció vàlida, torni a elegir una opció: \n")
        else: 
            return op

#Ejercicio 3
def ex1(): 
    a = int(input("Introdueix el primer número: "))
    b = int(input("Introdueix el segon número: "))
    if a > b:
        print("{} és major que {}".format(a,b))
    elif b > a:
        print("{} és major que {}".format(b,a))
    else:
        print("{} i {} són iguals".format(a,b))

#Ejercicio 4
def ex2():
    vocal = input("Introdueixi una vocal: ")
    match(vocal):
        case 'a':
            print("La vocal introduïda és una 'a'")
        case 'e':
            print("La vocal introduïda és una 'e'")
        case 'i':
            print("La vocal introduïda és una 'i'")
        case 'o':
            print("La vocal introduïda és una 'o'")
        case 'u':
            print("La vocal introduïda és una 'u'")
        case other: 
            print("Opció no vàlida!")

#Ejercicio 5
def ex3():
    a = []
    b = []
    for i in range(3):
        a.append (input("Introdueixi una paraula: "))
    for e in a:
        b.append(len(e))
    print("Les longituds de la llista {} són {}".format(a,b))

#Ejercicio 6
def ex4():
    for i in range(1,10,2):
        print(i)

#Ejercicio 7
def ex5():
    llista = [1,2,3,4,5]
    dic = {}
    for i,e in enumerate(llista):
        dic[i] = e
    print("De la llista {} hem creat el diccionari {}".format(llista, dic))

#Ejercicio 8
def ex6(llista,c):
    b = []
    for e in llista:
        if c in e:
            b.append(e)
    print("De la llista {}, les següents {} contenen el caràcter {}".format(llista,b,c))

#Ejercicio 9
def ex7():
    a = [3, 4, 6, 8, 9]
    b = list(map(lambda x: x+10, a))
    print(b)

#Ejercicio 10
def ex8():
    a = [2,6,3,4,8]
    b = [x ** 2 for x in a if x%2==1]
    print(b)
#Ejercicio 11
def ex9(): 
    a = ["Clara", "Maria", "Sebas"]
    b = list(map(lambda x: x[::-1], a))
    print(b)
#Ejercicio 12
def ex10():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = list(zip(a,b))
    print(c)
#Ejercicio 13
def ex11():
    a = [1, 2, 3, 4, 5]
    b = list(filter(lambda x: x%2==1, a))
    #puedo dejar solo un print(b)
    print("Els nombres imparells de la llista {} són: {}".format(a,b)) 

#Ejercicio 14
def ex12():
    class Ordinador():
        def __init__(self,tipus,pantalla):
            self.tipus = tipus
            self.pantalla = pantalla
        def getTipus(self):
            print(self.tipus)
        def getPantlla(self):
            print(self.pantalla)

#Ejercicio 15
    class Portatil(Ordinador):
        def getTipus(self):
            print("Soc un portatil")
        def getPantalla(self):
            print("La meva pantalla és de 15 polzades")
#Ejercicio 16
    class Tablet(Ordinador):
        def getTipus(self):
            print("Soc una tablet")
        def getPantalla(self):
            print("La meva pantalla és de 9 polzades")
#Ejercicio 17
    class Servidor(Ordinador):
        def getTipus(self):
            print("Soc un servidor")
        def getPantalla(self):
            print("La meva pantalla és de 21 polzades")
#Ejercicio 18
    class PC(Ordinador):
        def getTipus(self):
            print("Soc un PC")
        def getPantalla(self):
            print("La meva pantalla és de 27 polzades")
#Ejercicio 19
    llista = [Portatil('soc un portatil', 'La meva pantalla és de 15 polzades'),
              Tablet('Soc una tablet', 'La meva pantalla és de 9 polzades'), 
              Servidor('Soc un servidor', 'La meva pantalla és de 21 polzades'),
              PC('Soc un PC', 'La meva pantalla és de 27 polzades')]
    for e in llista:
        e.getTipus()
        e.getPantalla()
        
#Ejercicio 20
def ex13():
    with open("/home/cicles/AO/Python/Tarea11Python/ex20.txt", "w") as f:
        for e in range(10):
            f.write(str(e)+",")
    a = []
    with open("/home/cicles/AO/Python/Tarea11Python/ex20.txt", "r") as f: 
        for e in f:
            a.append(e)
        print(a)
    
#Programa Principal
op = 1
while op != 14:
    op = menu()
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            l = ["Hola","Adeu","Hello","bye","alt","Baix"]
            c = "a"
            ex6(l,c)
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()
        case 12:
            ex12()
        case 13:
            ex13()
        case 14:
            print("Programa acabat, que ho passi molt bé i gràcies per utilitzar-me!")