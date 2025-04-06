# PROBLEM STATEMENT:

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


# SOLUTION 👇:

def subtract_seven(num: int) -> int:
    return num - 7 

def main():
    num = 7
    print("this should be zero", subtract_seven(num))

if __name__ == '__main__':
    main()
