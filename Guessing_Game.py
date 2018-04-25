# CREATE A GUESSING NUMBER GAME INTERFACE
## Player gets to guess a random number from 1 to 10 for 3 times, the prize is a crystal ball!

import random

# Generate a random number from 1-10 and store it in a variable
num = random.randint(1,10)

# Ask for player input
guess = int(input("Guess a number from 1-10: "))

# Set initial guessing time
times = 1

# Repeating until the player used all 3 times
while guess != num:
	guess = int(input("Try again: "))
	times = times + 1
	if times == 3:
		break
	else:
		continue
		
if guess == num:
	print("Congrats! You win!")
else:
	print("You lose, the number is: ", num)
