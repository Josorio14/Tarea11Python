def lenp(frase):
    b = frase.split(" ")
    c =list(map(len, b))
    print("la frase: '{}' tiene las siguientes longitudes {} ".format(frase, c))

#Programa principal
a = "Esto es una frase donde trabajaremos"
lenp(a)