# PROBLEM STATEMENT:

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# SOLUTION👇


def get_first_element(first):
    print(first[0])

def get_element():
    first = []
    element = input("Enter an element or press Enter to stop:")
    while element != "":
        first.append(element)
        element = input("Enter an element or press Enter to stop:")

    return first

def main():
    firstElement = get_element()
    get_first_element(firstElement)

if __name__ == '__main__':
    main()

