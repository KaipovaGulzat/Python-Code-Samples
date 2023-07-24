#Gulzat Kaipova
#7/23/2023
#a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

import math

def main():
    # Ask the user for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))

    # Compute the area of the circle using the formula: A = π * r^2
    area = math.pi * radius**2

    # Print the result
    print(f"The area of the circle with radius {radius} units is: {area:.2f} square units.")

if __name__ == "__main__":
    main()

