def print_welcome_message():
    print(
        "Welcome to MindNest! A tool designed to help you stay focused and productive."
    )


def get_user_input():
    try:
        work_time = int(input("Enter work time (in minutes): "))
        rest_time = int(input("Enter rest time (in minutes, or 0 for no rest): "))
        cycles = int(input("Enter the number of cycles: "))
    except ValueError:
        print("Invalid input, please enter numbers only.")
        return get_user_input()

    return work_time, rest_time, cycles
