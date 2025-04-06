# PROBLEM STATEMENT:

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


# SOLUTION 👇

def main():
    list_of_input = []
    value = input("\nEnter a value:")
    while value:
        list_of_input.append(value)

        value =input("\nEnter a value:")

    print(f"\nHere's the list of your given values: {list_of_input}\n")


if __name__ == '__main__':
    main()