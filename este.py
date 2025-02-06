import time
mybool = True
mystring = "Hello World"
timer = 1
counter = 0

x = "Bonjour"
w = "allo"
while mybool:
    if counter == 0:
        print(x)
        counter += 1
        time.sleep(timer)
    else :
        print(w)
        counter -= 1
        time.sleep(timer)
