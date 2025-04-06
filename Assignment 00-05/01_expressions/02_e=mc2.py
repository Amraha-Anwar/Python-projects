# PROBLEM STATEMENT
# This program calculates the energy equivalent of a given mass using Einstein's mass-energy equivalence formula:
# E = m * c^2
# where:
#   - E represents energy (in joules),
#   - m represents mass (in kilograms),
#   - C is the speed of light, which is approximately 299,792,458 meters per second.
#
# The program continuously prompts the user to enter a mass value and then computes the corresponding energy.



# SOLUTION 👇

from rich.console import Console
# the speed of light as a constant (in meters per second)
C: int = 299792458  

def main():
    console = Console()
    print("-----------------------------------------------------")
    print("                Energy Calculation                   ")
    print("-----------------------------------------------------")

    
    mass: float = float(input("Enter the mass in kilograms: "))

    # Calculate energy using Einstein's formula: E = m * C^2
    energy: float = mass * (C ** 2)

    # Displaying the equation and values
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")

    
    console.print(f"[green]\n{energy} joules of energy.\n[/green]")

if __name__ == '__main__':
    main()
