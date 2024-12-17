try:
    y=1/10

# Excepción más concreta
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema al realizar la operación")

# Excepción para cualquier otro problema.
except:
    print("Algo ha cascao aqui...")
    
print("FIN")