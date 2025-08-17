import os
from OpenSSL import crypto
import random
import string
from cryptography.hazmat.primitives.serialization import pkcs12, load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import serialization

# Función para generar una contraseña aleatoria
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Función para crear un certificado autofirmado
def create_self_signed_cert(subject, cert_name):
    # Generar par de claves
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Crear un certificado autofirmado
    cert = crypto.X509()
    cert.get_subject().C = subject.get('C', 'US')[:2]  # Código de país debe ser de 2 letras
    cert.get_subject().ST = subject.get('ST', 'State')[:128]  # Nombre del estado debe ser de máximo 128 caracteres
    cert.get_subject().L = subject.get('L', 'City')[:128]  # Nombre de la localidad debe ser de máximo 128 caracteres
    cert.get_subject().O = subject.get('O', 'Organization')[:64]  # Nombre de la organización debe ser de máximo 64 caracteres
    cert.get_subject().OU = subject.get('OU', 'Organizational Unit')[:64]  # Nombre de la unidad organizativa debe ser de máximo 64 caracteres
    cert.get_subject().CN = cert_name[:64]  # Nombre común debe ser de máximo 64 caracteres
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Crear directorio con el nombre del certificado
    dir_name = cert_name
    os.makedirs(dir_name, exist_ok=True)

    # Guardar la clave privada en un archivo .key
    key_filename = os.path.join(dir_name, f"{cert_name}.key")
    with open(key_filename, 'wb') as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    # Guardar el certificado en un archivo .cer
    cer_filename = os.path.join(dir_name, f"{cert_name}.cer")
    with open(cer_filename, 'wb') as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    return key_filename, cer_filename, key, cert

# Función para crear un archivo .p12 a partir de una clave privada y un certificado usando la biblioteca cryptography
def create_p12(key, cert, password, p12_filename):
    p12_data = pkcs12.serialize_key_and_certificates(
        name=p12_filename.encode(),
        key=load_pem_private_key(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, key),
            password=None,
        ),
        cert=load_pem_x509_certificate(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert),
        ),
        cas=None,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    with open(p12_filename, 'wb') as f:
        f.write(p12_data)

# Pedir al usuario el nombre del certificado (que también será el nombre de la carpeta)
cert_name = input("Introduce el nombre del certificado (esto también será el nombre de la carpeta): ")

# Pedir al usuario los detalles del subject
subject = {}
subject['C'] = input("Introduce el nombre del país (código de 2 letras) [US]: ")
subject['ST'] = input("Introduce el nombre del estado o provincia (nombre completo) [State]: ")
subject['L'] = input("Introduce el nombre de la localidad (por ejemplo, ciudad) [City]: ")
subject['O'] = input("Introduce el nombre de la organización (por ejemplo, empresa) [Organization]: ")
subject['OU'] = input("Introduce el nombre de la unidad organizativa (por ejemplo, sección) [Organizational Unit]: ")

# Crear certificado autofirmado
key_filename, cer_filename, key, cert = create_self_signed_cert(subject, cert_name)

# Generar una contraseña aleatoria
password = generate_password()

# Guardar la contraseña en un archivo .txt con el mismo nombre que el archivo .key
password_filename = key_filename.replace('.key', '.txt')
with open(password_filename, 'w') as f:
    f.write(password)

# Mostrar la contraseña
print(f"La contraseña es: {password}")

# Crear un archivo .p12 a partir de la clave privada y el certificado usando la biblioteca cryptography
p12_filename = os.path.join(cert_name, f"{cert_name}.p12")
create_p12(key, cert, password, p12_filename)

print(f"El archivo .p12 ha sido creado: {p12_filename}")
