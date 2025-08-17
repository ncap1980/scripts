def calcular_letra_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni % 23]

def validar_dni(dni):
    if len(dni) != 9:
        return False
    dni_numeros = dni[:-1]
    letra = dni[-1]
    if not dni_numeros.isdigit():
        return False
    return calcular_letra_dni(int(dni_numeros)) == letra

# Pedir el DNI por pantalla y validar
dni = input("Introduce un DNI para validar: ").upper()
if validar_dni(dni):
    print(f"El DNI {dni} es válido.")
else:
    print(f"El DNI {dni} no es válido.")
