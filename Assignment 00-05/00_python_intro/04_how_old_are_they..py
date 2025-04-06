# PROBLEM STATEMENT

# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7

# SOLUTION 👇
def main():
    print("🎉 Welcome to the Age Riddle Solver! 🎉")
    print("--------------------------------------------------")
    print("     🔢 Let's find out the ages of our friends! 🔢")
    print("--------------------------------------------------")

    # Storing ages
    anton: int = 21
    beth: int = 6 + anton
    chen: int = 20 + beth
    drew: int = chen + anton
    ethan: int = chen

    # Displaying ages
    print("\n🧑‍🎓 Meet the group and their ages! 🎂\n")
    print(f"👦 Anton is {anton} years old.")
    print(f"👧 Beth is {beth} years old, 6 years older than Anton!")
    print(f"👨 Chen is {chen} years old, 20 years older than Beth.")
    print(f"🧑‍🏫 Drew is {drew} years old, as old as Chen plus Anton.")
    print(f"👨‍🦰 Ethan is {ethan} years old, the same as Chen.")

    print("\n🎊 That's the mystery solved! 🎊")

if __name__ == "__main__":
    main()
