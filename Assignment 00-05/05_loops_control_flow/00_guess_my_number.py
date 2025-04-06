# PROBLEM STATEMENT:

# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

# SOLUTION 👇

import random 

def main():
    secretNumber = random.randint(1, 99)

    print("I am thinking of a number between 0 and 99, you have to guess it :D")

    user_guess = int(input('Enter a number: '))
    while user_guess != secretNumber:
        if user_guess < secretNumber:
            print('Your guess is too low!')
        else:
            print('Your guess is too high!')

        print()
        user_guess = int(input('Enter a new guess: '))

    print("Wohoo You Won!! The number was " + str(secretNumber))

        
if __name__ == '__main__':
    main()
