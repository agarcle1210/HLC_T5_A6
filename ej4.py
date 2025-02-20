def es_palindromo(cadena):
    
    if len(cadena) <= 1:
        return True
    
    if cadena[0] != cadena[-1]:
        return False
    
    return es_palindromo(cadena[1:-1])

print(es_palindromo("oso"))
print(es_palindromo("hola")) 