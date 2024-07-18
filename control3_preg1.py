def solo_numeros(n):

    try:
        float(n)
        return True
    
    except:
        return False
    
n =input("Ingrese una Palabra: ")
print(solo_numeros(n))



