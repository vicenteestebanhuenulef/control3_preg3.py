def potencia(num,exp):
 
 if exp==0:
    return 1
 else:

    res= num*potencia(num,exp-1)
    return res

print(potencia(3,9))