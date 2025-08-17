import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate data
data = []
for _ in range(100):
    date = fake.date()
    country = fake.country()
    province = fake.state()
    code = fake.zipcode()
    data.append((date, country, province, code))

# Generate SQL insert statements
insert_statements = "INSERT INTO datos (Fecha, Pais, Provincia, Codigo) VALUES\n"
insert_statements += ",\n".join([f"('{d[0]}', '{d[1]}', '{d[2]}', '{d[3]}')" for d in data])
insert_statements += ";"

# Save to a file
with open("insert_statements.sql", "w") as file:
    file.write(insert_statements)

print("SQL insert statements generated and saved to insert_statements.sql")
