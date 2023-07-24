#Gulzat Kaipova
#7/23/2023
#Below is a Python program to calculate miles per gallon (MPG) for a car

def main():
    # Ask the user for the number of miles driven
    miles_driven = float(input("Enter the number of miles driven: "))

    # Ask the user for the number of gallons used
    gallons_used = float(input("Enter the number of gallons used: "))

    # Calculate miles per gallon (MPG) using the formula: MPG = miles_driven / gallons_used
    mpg = miles_driven / gallons_used

    # Print the result
    print(f"Your car's MPG is: {mpg:.2f} miles per gallon.")

if __name__ == "__main__":
    main()
