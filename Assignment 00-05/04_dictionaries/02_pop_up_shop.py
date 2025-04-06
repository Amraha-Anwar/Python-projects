# PROBLEM STATEMENT:

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):
# How many (apple) do you want?: 2
# How many (durian) do you want?: 0
# How many (jackfruit) do you want?: 1
# How many (kiwi) do you want?: 0
# How many (rambutan) do you want?: 1
# How many (mango) do you want?: 3
# Your total is $99.5

# SOLUTION 👇

def main():
    fruits = {
        "Apple" : 5,
        "Banana": 3,
        "Grapes" : 8,
        "Pomegranate" : 9.9,
        "Guava" : 80,
        "Oranges" : 33.6
    }

    totalAmount = 0

    for fruitName in fruits:
        price = fruits[fruitName]
        quantity_bought = int(input(f"How many {fruitName} do you want to buy?: "))
        totalAmount += (price * quantity_bought)

    
    print("Your Total is $" + str(totalAmount))


if __name__ == '__main__':
    main()