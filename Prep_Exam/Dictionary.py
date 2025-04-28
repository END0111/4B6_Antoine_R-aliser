composants = [{"price": 10,"quantity": 100,"backorder": 1000},
              {"price": 10,"quantity": 200,"backorder": 100},
              {"price": 10,"quantity": 300,"backorder": 10}]
for composant in composants:
    print(composant["price"]*composant["quantity"] + composants["backorder"])
    
# dictionary components need {} to be registered in the list
