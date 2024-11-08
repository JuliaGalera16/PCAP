from pares import imprime_pares as impp


line= input("Ingresa una linea de numeros, sepáralos con espacios:")
strings=line.split()
total=0

try:
    for substr in strings:
        total +=float(substr)
    print("El total es:", total)
except:
    print("Error: "+ substr+ " no es un numero")
    

impp(strings)        