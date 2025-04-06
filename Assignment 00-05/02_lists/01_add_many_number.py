# PROBLEM STATEMENT:
# Write a function that takes a list of numbers and returns the sum of those numbers.


# SOLUTION👇
def sum_of_numbers(numbers)-> int:
    sum : int = 0
    for number in numbers:
        sum += number

    return sum

    
def main():
    numbers : list[int] = [1, 2, 3]
    addition = sum_of_numbers(numbers)
    print(f"The sum of {numbers} is: {addition}")

if __name__ == '__main__':
    main()
