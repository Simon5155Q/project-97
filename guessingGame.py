import random

print("This is a guessing game, pick a number between 1 and 9.")
randNum = random.randint(1,9)
# print(randNum)

i = 0
inp = int(input("enter your number: ")) 
while i < 5:
    if(inp > randNum):
        inp = int(input("Sorry your number was too high, try lower: "))
        i = i + 1       

    if(inp < randNum):
        inp = int(input("Sorry your number was too low, try higher: "))
        i = i + 1

    if(randNum == inp):
        print("You won!")
        break
        
    
if(i >= 5):
    print("You Lost :( the number was: ",randNum)


