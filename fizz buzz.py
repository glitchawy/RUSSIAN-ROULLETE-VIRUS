
def choose(decesion):
    print("what mode u wanna play\n1-for one shot\n2-for range game")
    decesion=int(input("i want to play:"))
    if decesion==1:
        print("hello to fizz buzz game")
        fizz_buzz(int(input("type a num")))
    elif decesion==2:
        print("hello to fizz buzz game")
        fizz_buzz2(0,0)

def fizz_buzz(num):
    if num%15==0:
        print("fizz buzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
       print("buzz")
    else :
        print("invalid")
        fizz_buzz(int(input("type a num")))
    new_try=input("wanna play again?(y/n)")
    if new_try=="y":
       fizz_buzz(int(input("type a num")))
    elif new_try=="n":
        print("thnx for using me")
def fizz_buzz2(range_start,range_end):
    range_start=int(input("ur start:"))
    range_end=int(input("ur end:"))
    for i in range(range_start,range_end):
        if i % 15 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print("invalid")
            fizz_buzz2(int(input("ur start:")),int(input("ur end:")))
        new_try = input("wanna play again?(y/n)")
        if new_try == "y":
            fizz_buzz2(int(input("ur start:")), int(input("ur end:")))
        elif new_try == "n":
            print("thnx for using me")

choose(0)