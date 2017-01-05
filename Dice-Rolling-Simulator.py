import random
print("Pres Yes to roll dices!")
f=input()
if f=="Yes":
    k="Y"
    while k=="Y":
        a=random.randrange(1,6)
        b=random.randrange(1,6)
        print("your Dice numbers are ",a," and ",b)
        print("Would you like to roll again! Then Enter Y character to continue or enter any character to finish!!")
        k=input()
        if k=="Y":
            continue
        else:
            break
else:
    print("Process is finished!")
