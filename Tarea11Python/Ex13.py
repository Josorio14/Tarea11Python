class Animal():
    def __init__(self, atributo, edad):
        self.atributo=atributo
        self.edad= edad
    def hablar(self):
        pass
    def moveremos(self):
        pass
    def quien_soy(self):
        print("Soy un animal")

class Caballo(Animal):
    def hablar(self):
        print("iiii")
    def moveremos(self):
        print("Me muevo trotando")
    def quien_soy(self):
        print("Soy un caballo")

class Delfin(Animal):
    def hablar(self):
        print("IchIchIch")
    def moveremos(self):
        print("Me muevo nadando")
    def quien_soy(self):
        print("Soy un delfin")

class Abeja(Animal):
    def hablar(self):
        print("Sssss")
    def moveremos(self):
        print("Me muevo volando")
    def quien_soy(self):
        print("Soy un abeja")
    def picar(self):
        print("Si m'empenyes et picaré!")

class Humano(Animal):
    def __init__(self, nombre, atributo, edad):
        self.nombre= nombre
        self.nombre= atributo
        self.nombre= edad

    def hablar(self):
        print("Hola")
    def moveremos(self):
        print("Me muevo caminando")
    def quien_soy(self):
        print("Soy un humano")

#Otro tipo de clase
class Centauro(Humano, Caballo):
    def hablar(self):
        print("Hola")
    def moveremos(self):
        print("Me muevo trotando")
    def quien_soy(self):
        print("Soy un centauro")

#Otro tipo de clase
class Chiquillo(Humano):
    def __init__(self, nombre, atributo, edad, listpadres):
        self.nombre= nombre
        self.atributo= atributo
        self.edad= edad
        self.listpadres= listpadres

    def hablar(self):
        print("Guaa Ueeeua")
    def moveremos(self):
        print("Me muevo gateando")
    def quien_soy(self):
        print("Soy un Chiquillo")
    def nombre_padres(self):
        for e in self.listpadres:
            print(e.nombre)

#Otro tipo de clase
class Xou(Animal):
    def hablar(self):
        print("Xou")
    def moveremos(self):
        print("Me muevo haciendo un xou")
    def quien_soy(self):
        print("Soy un Xou")

#Programa Principal 

a = [Caballo("marron","4 anys"),
    Delfin("Gris","10"), 
    Abeja("Negra y amarilla", "0,5"), 
    Humano("Sibila","Cristiano","7"), 
    Centauro("Fiona","Marron","18"),
    Chiquillo("Jordi","Moreno","9",["Fiona","Marc"]),
    Xou("xou","7")]

for e in a:
    e.hablar()
    e.moveremos()
    e.quien_soy()