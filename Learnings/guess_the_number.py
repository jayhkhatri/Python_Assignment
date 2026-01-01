"""
create a simple number guessing game.
the user gets 10 chances to guess a number.
If the user gets the number before 10 chances, stop asking from the user, say congrats and end the game
If the user never guesses the number, ask them 10 times end the game.
"""
import random

num = random.randint(1,50)
i=10
A =False
print('the seceret number is between 1 to 50')
print(f"you have {i} attemps left")

for count in range(i):
    inp = int(input('Enter your guess: '))
    if inp == num:
        print(f"congratulation, {num} is correct")
        A = True
        break
    else:
        if inp > num:
            print(f"your guess is too high")
        else:
            print(f"your guess is too low")
        print('your guess is wrong! try again')
        print(f"you have {i-(count+1)} attempts left")
        A = False
if A:
    print('you win')
else:
    print('you lose')
    print(f"correct answer is {num} ")
