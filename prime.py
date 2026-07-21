number = input("Enter a number: ")
for i in range(2, int(number)):
    if int(number) % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")   