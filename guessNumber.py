#number quessing game
#when starting, input also with the max ammount of numbers in range
#it will create number in that range, then you guess

import sys
import random

def checknumber(x, num):
    if(x == num):
        return "correct"
    else:
        return "wrong"

def convertInput(y):
    try:
        y = int(str(a))
        return y;
    except:
        print("Invalid input type, expected number")
        sys.exit();
        

if __name__ == "__main__":
    a = (sys.argv[1])

str(a)
num = random.randrange(0, convertInput(a))
print("Guess number between 0 and", a)

x = input()
fin = convertInput(x)

print("You got the number", checknumber(fin ,num))
print("The number was: ", num);

