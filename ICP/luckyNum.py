luckyNum = 84
guess = 0
attempt = 0
correct = False

while(correct == False):
    guess = int(input("Guess a number 1 - 100: "))
    attempt += 1
    if(luckyNum == guess):
        print(guess, "is correct")
        correct = True

    elif(guess > luckyNum):
        print(guess, "is too large")

    else:
        print(guess, "is too small")
        

print("You got the lucky number in ", attempt, "attempts")