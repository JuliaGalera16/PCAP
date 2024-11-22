fecha=''
while True:
    fecha=input("Introduce tu fecha de nacimiento (AAAAMMDD)")
    if fecha.isnumeric():
        break
    print("Debes introducir bien tu fecha")
    
digito=0
suma=0

for c in fecha:
    suma +=int(c)

print(suma)
if len(str(suma))>1:
    for c in str(suma):
        digito+=int(c) 
else:
    digito =suma


print("Tu dígito vital es:", digito)  