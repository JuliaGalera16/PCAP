tablero =[]
sudoku_ok= False

for i in range(9):
    fila = input("Introduce fila #"+str(i)+ ":")
    if not fila.isnumeric():
        print("La fila contiene caracteres no numéricos")
        break
    elif sorted(fila)!=list("123456789"):
        print("La fila debe contener todos los dígitos del intervalo[1-9].")
        break
    else:
        sudoku_ok=True
        tablero.append(fila)
        
if sudoku_ok:
    print("El sudoku es válido")
else:
    print("El sudoku no es válido")