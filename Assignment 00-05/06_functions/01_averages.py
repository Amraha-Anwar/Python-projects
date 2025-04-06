# PROBLEM STATEMENT:

# Write a function that takes two numbers and finds the average between the two.


# SOLUTION 👇

def average(num1: float, num2: float):
    sum = num1 + num2

    return sum / 2

def main():
    avg_1 = average(2, 6)
    avg_2 = average(1, 11)

    final = average(avg_1, avg_2)

    print(f"average 1 : {avg_1}")
    print(f"average 2 : {avg_2}")
    print(f"Final : {final}")


if __name__ == '__main__':
    main()