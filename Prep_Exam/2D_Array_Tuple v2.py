composants = [(1000, 100, 10), (10, 20, 30), (1, 2, 3)],
def retournerTotal(quantities, prix, backorder):
    if quantities > 0:
        return (quantities * prix + backorder, True)
    return (quantities * prix + backorder, False)
for quantity, price, backorder in composants:
    total,error = retournerTotal(quantity, price, backorder)
    if error:
        print("Error")