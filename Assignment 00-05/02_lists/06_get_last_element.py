# PROBLEM STATEMENT:

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# SOLUTION👇

def get_last_element(last):
    print(last[-1]) 


def get_last():  
    last = []
    element = input("Please enter an element of the list or press enter to stop. ") 
    while element != "":
        last.append(element) 
        element = input("Please enter an element of the list or press enter to stop. ") 
    return last

def main():
    last = get_last()
    get_last_element(last)

if __name__ == '__main__':
    main()