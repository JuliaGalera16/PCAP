frase = input("Introduce una frase: ")
frase2 = (frase.lower()).replace(' ','')

if frase2 == frase2[::-1]:
     print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")
