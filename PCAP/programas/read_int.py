def read_int(prompt, min, max):
    while True:
        try:
            valor = int(input(prompt))
            if (valor >= -10 and valor <=10 ):
                return valor
        except ValueError:
            print("Por favor, ingrese un valor entero")
        except:
            print("FATAL ERROR")        
                
v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)

print("El número es: ", v)