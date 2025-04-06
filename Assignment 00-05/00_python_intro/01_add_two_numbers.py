# PROBLEM STATEMENT

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# 1-Prompt the user to enter the first number.
# 2-Read the input and convert it to an integer.
# 3-Prompt the user to enter the second number.
# 4-Read the input and convert it to an integer.
# 5-Calculate the sum of the two numbers.
# 6-Print the total sum with an appropriate message.

# SOLUTION 👇

def main():
    print("------------------------------------------------------------------------------------\n        ✨ This Program will gonna add numbers which you will input ✨        \n------------------------------------------------------------------------------------")
    number1 : str = input("Enter First Number:")
    number1 : int = int(number1)
    number2 : str = input("Enter Second Number:")
    number2 : int = int(number2)
    additon : int = number2 + number2
    print("\n------------------------------------------------------------------------------------\n        ✨ The Sum of your given numbers is: " + str(additon) + " ✨        \n------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()