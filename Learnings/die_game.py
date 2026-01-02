"""
write a program to simulate a roll of a die/dice
"""
import random

print("Welcome to the game of rolling the dice")

while True:
    choice = input("Press 'enter' to roll a dice or 'q' to end: ")
    choice = choice.strip()
    choice = choice.lower()
    if choice == 'q':
        print("Thanks for playing the game, Goodbye")
        break
    elif choice == '':
        roll = random.randint(1,6)
        print(f"your number is {roll}")
    else:
        print("Please enter a valid input")

