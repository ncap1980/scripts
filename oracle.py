import cx_Oracle
import csv
import os
import base64

# Ruta del archivo donde se guardar  las credenciales cifradas
CREDENTIALS_FILE = "credentials.txt"

def get_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = file.readline()
            username, password = base64.b64decode(credentials).decode().split(":")
    else:
        print("Ingrese las credenciales para la base de datos:")
        username = input("Usuario: ")
        password = input("Contrase : ")

        credentials = f"{username}:{password}"
        encrypted_credentials = base64.b64encode(credentials.encode())

        with open(CREDENTIALS_FILE, 'w') as file:
            file.write(encrypted_credentials.decode())

    return username, password

def connect_to_oracle():
    username, password = get_credentials()
    connection = cx_Oracle.connect(username, password, 'localhost:1521/ORCL')
    return connection

def download_data_to_csv(start_date, end_date):
    connection = connect_to_oracle()
    cursor = connection.cursor()

    query = f"SELECT * FROM tsa_traces2d WHERE timestamp BETWEEN TO_DATE(:start_date, 'YYYY-MM-DD') AND TO_DATE(:end_date, 'YYYY-MM-DD')"
    cursor.execute(query, start_date=start_date, end_date=end_date)

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    download_data_to_csv(start_date, end_date)
    