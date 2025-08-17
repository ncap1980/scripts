from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

# Función para cargar el CSR y la clave privada desde archivos
def load_csr_and_key(csr_file, key_file):
    with open(csr_file, 'rb') as f:
        csr = x509.load_pem_x509_csr(f.read())
    with open(key_file, 'rb') as f:
        key = serialization.load_pem_private_key(f.read(), password=None)
    return csr, key

# Función para crear un nuevo CSR con un sujeto modificado
def create_modified_csr(csr, key, new_subject, csr_file):
    csr_builder = x509.CertificateSigningRequestBuilder().subject_name(new_subject)
    for extension in csr.extensions:
        csr_builder = csr_builder.add_extension(extension.value, extension.critical)
    new_csr = csr_builder.sign(key, hashes.SHA256())

    with open(csr_file, 'wb') as f:
        f.write(new_csr.public_bytes(serialization.Encoding.PEM))

# Ruta a los archivos del CSR y la clave privada
csr_file = 'C:/Users/alesio/SandraCert/SandraCert.csr'
key_file = 'C:/Users/alesio/SandraCert/SandraCert.key'

# Cargar el CSR y la clave privada
csr, key = load_csr_and_key(csr_file, key_file)

# Definir el nuevo sujeto para el CSR
new_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

# Crear el CSR modificado
create_modified_csr(csr, key, new_subject, csr_file)

print(f"El archivo CSR ha sido modificado: {csr_file}")
