#Gulzat Kaipova
#7/23/2023
#a Python program that calculates the day of the week you will return on after your holiday, given the starting day number and the length of your stay:

def get_return_day(starting_day, length_of_stay):
    # Calculate the total number of days including the stay duration
    total_days = starting_day + length_of_stay

    # Calculate the day of the week for the return day (0: Sunday, 1: Monday, ..., 6: Saturday)
    return_day = total_days % 7

    return return_day

def main():
    # List to map day numbers to day names
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Ask the user for the starting day number (0: Sunday, 1: Monday, ..., 6: Saturday)
    starting_day = int(input("Enter the starting day number (0 - Sunday, 1 - Monday, ..., 6 - Saturday): "))

    # Ask the user for the length of the stay
    length_of_stay = int(input("Enter the length of your stay in nights: "))

    # Calculate the day of the week for the return day
    return_day_number = get_return_day(starting_day, length_of_stay)

    # Get the corresponding day name from the list
    return_day_name = days_of_week[return_day_number]

    # Print the result
    print(f"You will return on {return_day_name}.")

if __name__ == "__main__":
    main()


