from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

# Función para cargar el certificado y la clave privada desde archivos
def load_cert_and_key(cert_file, key_file):
    with open(cert_file, 'rb') as f:
        cert = x509.load_pem_x509_certificate(f.read())
    with open(key_file, 'rb') as f:
        key = serialization.load_pem_private_key(f.read(), password=None)
    return cert, key

# Función para crear una solicitud de firma de certificado (CSR)
def create_csr(cert, key, csr_file):
    csr = x509.CertificateSigningRequestBuilder().subject_name(
        cert.subject
    ).sign(key, hashes.SHA256())

    with open(csr_file, 'wb') as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

# Ruta a los archivos del certificado y la clave privada
cert_file = 'C:/Users/alesio/SandraCert/SandraCert.cer'
key_file = 'C:/Users/alesio/SandraCert/SandraCert.key'
csr_file = 'C:/Users/alesio/SandraCert/SandraCert.csr'

# Cargar el certificado y la clave privada
cert, key = load_cert_and_key(cert_file, key_file)

# Crear la solicitud de firma de certificado (CSR)
create_csr(cert, key, csr_file)

print(f"El archivo CSR ha sido creado: {csr_file}")
