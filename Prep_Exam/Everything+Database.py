import sqlite3

conn = sqlite3.connect('Storage.db')

cursor = conn.cursor()

# Create a table to store the components

class Component:
    def __init__(self, type, price, quantity, Available_in_backorder, backorder):
        self.type = type
        self.price = price
        self.quantity = quantity
        self.Available_in_backorder = Available_in_backorder
        self.backorder = backorder
composants = [Component("bobine", 12, 10, True, 100),
              Component("condensateur", 120, 10, False, 0),
              Component("LED", 100, 10, False, 0)]

for composant in composants:
    Total = composant.price*composant.quantity + composant.backorder
    print(composant.price)
    print(Total)
    cursor.execute("Create Table IF NOT EXISTS Components (type TEXT, price INTEGER, quantity INTEGER, Available_in_backorder BOOLEAN, backorder INTEGER)")
    cursor.execute("INSERT INTO Components (type, price, quantity, Available_in_backorder, backorder) VALUES (?, ?, ?, ?, ?)", (composant.type, composant.price, composant.quantity, composant.Available_in_backorder, composant.backorder))
    conn.commit()
