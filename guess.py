import random
a = random.randint(1, 100)
while True:
    guess = int(input("enter your guess: "))
    if a > guess:
        print("Too low")
    elif a < guess:
        print("Too high")
    else :
        print("Correct!!!")
        break