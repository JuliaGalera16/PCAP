# cifrado Cesar
text = input("Ingresa tu mensaje: ")

shift2 =0
while shift ==0:
    try:
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25):"))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        print("ERROR: ¡Valor inválido!")
        shift = 0
        
text= text.upper()

cipher = ''    
for char in text:
    
   code = ord(char) + shift
   primero = ord('A')
   shift2 += (code - primero) % 26
   cipher += char(shift)
   

print(cipher)