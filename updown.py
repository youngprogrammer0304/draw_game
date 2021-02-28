from random import * 
from time import sleep

print("\tUPDOWN\n") 
print("setting\n")
print("chance")
e = int(input(""))
print("limit")
f = int(input("")) #here ~
g = int(input("")) #from
a = randint(f, g)
print("start game")
sleep(3)
for c in range(1, e + 1):
    b = int(input("input : ")) 
    if a < b:
        print("DOWN") 
    elif a > b:
        print("UP")
    else:
        print("SUCCES")
        break
if b != a:
    print("FAIL")
input("press key to quit...")    

