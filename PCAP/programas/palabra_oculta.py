palabra = input("Introduce la palabra a buscar:").upper()
grupo= input("Introduce el grupo de caracteres:").upper()

contiene= True
posicion=0

for c in palabra:
    pos= grupo.find(c, posicion)
    
    if pos < 0:
        contiene = False
        break
    posicion=pos +1
    
if contiene:
    print("La palabra contiene el grupo de caracteres")
else:
    print("La palabra no contiene el grupo de caracteres")
        
        