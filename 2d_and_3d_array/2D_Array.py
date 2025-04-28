matrice = [[255, 255, 0], 
           [0, 255, 255], 
           [255, 0, 255]]
for x in matrice:
    step = 0
    for y in x:
        step = step + 1
        if step == 1:
            print("R:" + str(y))
        if step == 2:
            print("G:" + str(y))
        if step == 3:
            print("B:" + str(y))

       
