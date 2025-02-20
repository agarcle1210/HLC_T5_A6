numeros = [1, 2, 3, 4, 5, 6]

def suma_pares(numeros):
    pares=0
    for i in numeros:
        if i % 2==0:
            pares+=i
    return pares
 
print(suma_pares(numeros))