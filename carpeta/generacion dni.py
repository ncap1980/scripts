def calcular_letra_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni % 23]

def generar_dni_ficticio():
    import random
    dni_numeros = random.randint(10000000, 99999999)
    letra = calcular_letra_dni(dni_numeros)
    return f"{dni_numeros}{letra}"

# Generar 10 DNIs ficticios
for i in range(30):
    print(generar_dni_ficticio())
