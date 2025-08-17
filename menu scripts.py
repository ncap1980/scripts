import os

def menu():
    print("Seleccione una opción:")
    print("1. Comprobador DNI")
    print("2. Crear CSR")
    print("3. Generación DNI")
    print("4. Generador de Certificados")
    print("5. Modificar CSR")
    print("6. Visualizar CSR")
    print("7. Salir")

def run_script(script_name):
    os.system(f'python "{script_name}"')

while True:
    menu()
    choice = input("Ingrese su elección: ")

    if choice == '1':
        run_script('comprobador dni.py')
    elif choice == '2':
        run_script('crear csr.py')
    elif choice == '3':
        run_script('generacion dni.py')
    elif choice == '4':
        run_script('generador de certificados.py')
    elif choice == '5':
        run_script('modificar csr.py')
    elif choice == '6':
        run_script('visualizar csr.py')
    elif choice == '7':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
