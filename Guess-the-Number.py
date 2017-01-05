import random
number = random.randrange(0,100)
print("Enter Your Guess Number!")
guess = int(input())
while guess !=number:
    if guess < number:
        print(guess," is less than")
        print("Enter your new Guess!")
        guess = int(input())
        continue
    else:
        print(guess, " is greater than")
        print("Enter your new Guess!")
        guess = int(input())
        continue
if guess==number:
    print("You got the correct number! Congratulation!!")
