import random

def gun():
    bullets=int(input("how many bullets in the gun u want ?"))
    if bullets==1 or bullets==2:
        print("low risk ... hmmm")
        game()
    elif bullets==3 or bullets==4:
        print("oh!... u luv danger")
        game()
    elif bullets==5:
        print("one shot try !! ... ")
        game()


def game():
    kill_bullet=random.randint(1,6)
    print(kill_bullet)
    for i in range(1,6)
    input("press enter to pull the trigger:")

gun()




