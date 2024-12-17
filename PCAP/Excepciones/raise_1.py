def mal_asunto(n):
    # Genera una excepción de3 tipo "division por cero"
    raise ZeroDivisionError

try:
    mal_asunto(0)
except:
    print("¿Qué ha pasado")

print("FIN")