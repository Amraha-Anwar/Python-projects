# PROBLEM STATEMENT

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
# The equation you should use for converting from Fahrenheit to Celsius is the following:
# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# SOLUTION 👇

def main():
    print("🎉 Welcome to the mini unit converter 🎉")
    print("------------------------------------------------------------------------------------")
    print("        🌡️ This program is created to convert Fahrenheit to Celsius! 🌡️        ")
    print("------------------------------------------------------------------------------------")
    fahrenheit : str = input("Enter the Temperature in Fahrenheit:")
    fahrenheit : float = float(fahrenheit)
    celsius : float = (fahrenheit - 32) * 5.0/9.0
    print("\n------------------------------------------------------------------------------------")
    print(f"✅ The temperature {fahrenheit}°F is equal to {round(celsius, 2)}°C.")
    print("------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()