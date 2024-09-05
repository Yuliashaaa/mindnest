from core.timer import Timer


def display_greeting():
    print("\nWelcome to MindNest!")
    print(
        "A simple and intuitive tool designed to help you focus and be more productive."
    )
    print("Let's set up your first timer!\n")


def display_menu():
    print("\nGreat job! What would you like to do next?")
    print("1. Set a new timer")
    print("2. Run the same timer again")
    print("3. Exit")


def get_user_choice():
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid input. Please enter 1, 2, or 3.")


def main():
    display_greeting()  # Show greeting at the start

    work_time = int(input("Enter work time in minutes: "))
    rest_time = int(input("Enter rest time in minutes (or 0 to skip rest): "))
    cycles = int(input("Enter number of cycles: "))

    timer = Timer(work_time, rest_time, cycles)

    while True:
        timer.start()  # Start the timer

        # After the timer is done, display the menu
        display_menu()
        user_choice = get_user_choice()

        if user_choice == "1":
            # User wants to set a new timer, so ask for new inputs
            work_time = int(input("Enter new work time in minutes: "))
            rest_time = int(
                input("Enter new rest time in minutes (or 0 to skip rest): ")
            )
            cycles = int(input("Enter number of cycles: "))
            timer = Timer(work_time, rest_time, cycles)
        elif user_choice == "2":
            # User wants to run the same timer again, continue
            print("Restarting the same timer...")
        elif user_choice == "3":
            # User wants to exit
            print("Goodbye! Great work today!")
            break


if __name__ == "__main__":
    main()
