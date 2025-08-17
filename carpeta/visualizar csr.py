from cryptography import x509
from cryptography.hazmat.primitives import serialization

# Función para cargar y analizar el CSR
def load_csr(csr_file):
    with open(csr_file, 'rb') as f:
        csr = x509.load_pem_x509_csr(f.read())
    return csr

# Función para imprimir los detalles del CSR
def print_csr_details(csr):
    print("Subject:")
    for attribute in csr.subject:
        print(f"  {attribute.oid._name}: {attribute.value}")

    print("\nExtensions:")
    for extension in csr.extensions:
        print(f"  {extension.oid._name}: {extension.value}")

# Ruta al archivo CSR
csr_file = 'C:/Users/alesio/SandraCert/SandraCert.csr'

# Cargar y analizar el CSR
csr = load_csr(csr_file)

# Imprimir los detalles del CSR
print_csr_details(csr)
