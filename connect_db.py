import cx_Oracle,getpass

passw = getpass.getpass('Password1: ')
connection = cx_Oracle.connect("usuario", passw, "192.168.2.44/ORCLPDB1.localdomain", encoding="UTF-8")


print(passw)
