#Gulzat Kaipova
#7/23/2023
#A program that asks the user for their name and greets only two people with their name.
def main():
    # Ask the user for their name
    name = input("What is your name? ")

    # List of names to greet
    allowed_names = ["Gulzat", "Robyn"]

    # Greet the user with their name if their name is in the allowed_names list
    if name.lower() in [n.lower() for n in allowed_names]:
        print(f"Hello, {name}! Nice to meet you.")
    else:
        print("Access declined")

if __name__ == "__main__":
    main()

