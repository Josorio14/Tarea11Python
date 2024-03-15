#Ex 12 Tarea 11
import os 
compañeros = ["Jordi", "Claudia", "Joan", "Paula", "Anas", "Sebas", "Clara","Hugo","Oscar","Josep", "Marc", "Sergi", "Alvaro", "Fede", "Ian","Ayoub","David","Leiner"]

os.mkdir("/home/cicles/AO/Python/Tarea11Python/Prueba")
os.chdir("/home/cicles/AO/Python/Tarea11Python/Prueba")
with open ("Ex12.txt","w") as f:
    print("Fichero creado correctamente")
    for e in compañeros:
        f.write(e+"\n")

profesores = ["Pep Malle","Joan Carreras", "Rafaela Moll", "Lluis Vila","David Labiano"]
with open ("Ex12.txt","a+") as f:
    print("Fichero creado correctamente")
    for e in profesores:
        f.write(e+"\n")
a = []
with open ("Ex12.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)