#SNAKE WATER GUN
import random
def gameWin(comp,b):
     if comp==b:
        return None
     elif comp=='s':
        if b=='w':
           return False
        elif b=='g':
           return True
     elif comp=='w':
        if b=='g':
           return False
        elif b=='s':
           return True
     elif comp=='g':
        if b=='w':
           return True
        elif b=='s':
           return False
print(" Computer's turn : Snake(s) / Water(w) / Gun(g)")
randNo = random.randint(1,3)
if randNo==1:
     comp='s'
elif randNo==2:
     comp='w'
elif randNo==3:
     comp='g'
b=input("\nYour turn : Snake(s) / Water(w) / Gun(g)")
result=gameWin(comp,b)
print("Computer chose",{comp})
print("You chose",{b})
if result==None:
    print("\nThis is a tie")
elif result:
    print("\nYou win!!")
else:
    print("\nYou lose")
