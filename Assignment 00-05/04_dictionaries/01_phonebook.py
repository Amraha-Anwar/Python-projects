# PROBLEM STATEMENT:

# In this program we show an example of using dictionaries to keep track of information in a phonebook.


# SOLUTION 👇

def get_phone_numbers():
    phonebook = {}

    while True:
        name = input("Enter Name: ")
        if name == '':
            break

        number = input("Enter the Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " --> " + str(phonebook[name]))

def looking_up_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == '':
            break

        if name not in phonebook:
            print(f"{name} does not exist in phonebook :(")
        else:
            print(phonebook[name])

def main():
    phonebook = get_phone_numbers()
    print_phonebook(phonebook)
    looking_up_numbers(phonebook)


if __name__ == '__main__':
    main()