#Gulzat Kaipova
#7/23/2023
#Python program to convert degrees Fahrenheit to degrees Celsius

def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    # Ask the user to enter the temperature in Fahrenheit
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print the result
    print(f"{fahrenheit:.2f} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()

