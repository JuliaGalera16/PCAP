while True:
    text1=input("Introduce la primera palabra: ").upper()
    if not text1.isalpha():
        print("Error: " + text1 + " no es una palabra")
        break
    else:
        text2=input("Elige la segunda palabra: ").upper()
        if not text2.isalpha():
            print("Error: "+ text2 + " no es una palabra")
            break
  
        