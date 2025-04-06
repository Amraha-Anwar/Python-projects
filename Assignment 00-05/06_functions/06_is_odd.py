# PROBLEM STATEMENT:

# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

# SOLUTION 👇

def main():
    for i in range(10):
        if is_odd(i):
            print("odd")
        else:
            print("even")

def is_odd(value: int):
    remainder = value % 2
    return remainder == 1

if __name__ == '__main__':
    main()