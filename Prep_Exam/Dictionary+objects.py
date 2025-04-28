class Component:
    def __init__(self, price, quantity, backorder):
        self.price = price
        self.quantity = quantity
        self.backorder = backorder
composants = [Component(12, 10, 1000),
              Component(120, 10, 100),
              Component(100, 10, 10)]

for composant in composants:
    Total = composant.price*composant.quantity + composant.backorder
    print(composant.price)
    print(Total)