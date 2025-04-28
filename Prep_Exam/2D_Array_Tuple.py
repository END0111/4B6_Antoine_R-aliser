composants = [(1000, 100, 10), (10, 20, 30), (1, 2, 3)],
for quantity, price, backorder in composants:
    print(quantity)
    print(price)
    print(backorder)

def retournerTotal(quantities, prix, backorder):
    return (quantities * prix + backorder, "This is wrong")
for quantity, price, backorder in composants:
    total,error = retournerTotal(quantity, price, backorder)
    print(total)
    print(error)