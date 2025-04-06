# PROBLEM STATEMENT

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).


# SOLUTION 👇

def main():
    print("🌟🐾 Welcome to the Favorite Animal Program! 🐾🌟")
    print("------------------------------------------------------------------------------------")
    print("        🐆🐎🦌🦍 This program is created to know about your favorite animal! 🐆🐎🦌🦍        ")
    print("------------------------------------------------------------------------------------")

    animal: str = input("💭 What's your favorite animal? ").strip().capitalize()
    
    print(f"🤩 Wow! My favorite animal is also {animal}! 🐾✨ That's amazing!")

if __name__ == '__main__':
    main()
