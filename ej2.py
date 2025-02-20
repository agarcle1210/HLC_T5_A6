import random

def generar_contraseña(longitud):
   
    letras="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros="1234567890"
    caracteres_especiales="|@#~€¬!·$%&/()=?¿¡*¨[]{}-_;:,.<>"
    caracteres=letras+numeros+caracteres_especiales
    contraseña="".join(random.choice(caracteres) for i in range(longitud))
    return contraseña


print(generar_contraseña(random.randint(1,10))) 