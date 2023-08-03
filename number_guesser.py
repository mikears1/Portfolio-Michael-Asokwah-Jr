import random
a = 1
b = 10

p = "y"

while p == "y":
    n = random.randrange(a,b)
    guess = int(input("Enter any number between " + str(a) + " and " + str(b) + ": "))
    while n!= guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))


    print("you guessed it right!!")
    n = random.randrange(a,b)
    a = a*10
    b = b*10
    p = input("Play again? y/n: ")
    if p == "n":
        print("Thank you for playing!")

    else:
        guess = int(input("Enter any number between " + str(a) + " and " + str(b) + ": "))
        print(n)
        
  
