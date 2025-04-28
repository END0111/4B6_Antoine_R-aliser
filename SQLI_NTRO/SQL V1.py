import sqlite3

# Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect('home.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Create a table (if it doesn't exist)
cursor.execute("CREATE TABLE IF NOT EXISTS Car ( id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER, owner TEXT, Pressure_Tire_1 INTEGER, Pressure_Tire_2 INTEGER, Pressure_Tire_3 INTEGER, Pressure_Tire_4 INTEGER)")
 
# Créer du nouveau contenu
# Insert data into the table with placeholders ? allows you to insert data safely, preventing SQL injection.
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (1202, 'BMW', 'M4', 2022, 'Tom', 31, 31, 31, 31))
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (1324, 'Toyota', 'Corolla', 2023, 'Alice', 30, 30, 30, 30))
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (1234, 'Toyota', 'Corolla', 2020, 'Alice', 32, 32, 32, 32))
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (3344, 'Honda', 'Civic', 2019, 'Bob', 30, 30, 30, 30))
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (4455, 'Ford', 'Focus', 2021, 'Alice', 31, 31, 31, 31))
cursor.execute("INSERT INTO Car (id, make, model, year, owner, Pressure_Tire_1, Pressure_Tire_2, Pressure_Tire_3, Pressure_Tire_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (5566, 'Chevrolet', 'Malibu', 2022, 'Bob', 29, 29, 29, 29)) 
# Changer du contenu existant
cursor.execute("UPDATE Car SET model = 'Takoma', year= 2020 WHERE model = 'Corolla' AND make = 'Toyota' AND year = 2023")
cursor.execute("UPDATE CAR SET Pressure_Tire_1 = 30 WHERE model = 'Corolla' AND make = 'Toyota' AND year = 2020")
# Effacer Bob
cursor.execute("DELETE FROM Car WHERE make = 'Honda'")
cursor.execute("DELETE FROM Car WHERE make = 'Ford'")
# Save the changes made to the database. Without this, the insertions won't be permanent.
conn.commit()
 
# Query data from the table
cursor.execute("SELECT * FROM Car")
rows = cursor.fetchall()
 
# Print the results
for row in rows:
    print(row)