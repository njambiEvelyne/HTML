import random

# Display game rules
print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"]

while True:

    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # Validate user input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Please enter a valid choice (1-3): "))

    # User choice
    user_choice = choices[choice - 1]

    print("\nUser choice is:", user_choice)
    print("Now it's Computer's Turn...")

    # Computer choice
    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)
    print(user_choice, "vs", computer_choice)

    # Determine winner
    if choice == comp_choice:
        print("<== It's a Tie! ==>")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("<== User Wins! ==>")

    else:
        print("<== Computer Wins! ==>")

    # Play again
    while True:
        ans = input("\nDo you want to play again? (Y/N): ").lower()

        if ans in ['y', 'n']:
            break

        print("Please enter Y or N.")

    if ans == 'n':
        break

    print()

print("\nThanks for playing!")