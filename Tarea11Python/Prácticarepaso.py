def menu():
    opcion = 0
    while opcion<1 or opcion >5:
        print("""
        Menu principal: \n
        1. Programación estructurada
        2. Programación funcional
        3. Programación Orientada a Objetos
        4. Acceso a ficheros 
        5. Salir
         """)
        
        opcion = int(input("Selecciona la opción que quieras a ejecutar: \n"))
        if opcion<1 or opcion >5:
            print("Opción no valida")
        else:
            return opcion
    
def Programacion_estructurada():
    print("Muy bien, has entrado a la programacion_estructurada.\n \n")   

def Programación_funcional():
    print("Muy bien, has entrado a la programacion funcional.\n \n") 

def Programación_oo():
    print("Muy bien, has entrado a la Programación Orientada a Objetos. \n \n") 

def Acesso_ficheros():
    print("Muy bien, has entrado a la Acesso_ficheros. \n \n")      
#Programa Principal
op =1
while op!= 5:
    op=menu()
    match(op):
        case 1:
            Programacion_estructurada()
        case 2:
            Programación_funcional()
        case 3:
            Programación_oo()
        case 4:
            Acesso_ficheros()
        case 5:
            a = -1
            print("Gracias por su visita, vuelve al menu principal")
        case other:
            print("Opción no valida")
