# PROBLEM STATEMENT:

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


# SOLUTION 👇:

def in_range(n, low, high):
    return low <= n <= high 

def main():
    print("\nEnter a number and range (low and high) to check if it's within the range (inclusive).\n")
    
    n = int(input("Enter the number to check: ")) 
    low = int(input("Enter the lower bound: "))    
    high = int(input("Enter the upper bound: "))

    print(f"Result: {in_range(n, low, high)}") 

if __name__ == '__main__':
    main()

