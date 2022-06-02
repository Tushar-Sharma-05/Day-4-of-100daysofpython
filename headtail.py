from secrets import choice
import random
toss = int(input("Click 1 to start\n"))
if toss==1:
    random_side = random.randint(0, 1)
    if random_side==0:
        print("You got a head")
    else:
        print("You got a tail")
else:
    print("You have entered an invalid input")