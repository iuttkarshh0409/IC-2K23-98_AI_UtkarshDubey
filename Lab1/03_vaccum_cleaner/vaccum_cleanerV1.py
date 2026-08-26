current_state = ("Dirty", "Dirty", "A")
step_count = 0

print(f"\nInitial State: {current_state}")
print("Goal: Both rooms must be Clean")

while True:

    print("\n--- Available Operations ---")
    print("1. Suck")
    print("2. Move to Room 1")
    print("3. Move to Room 2")
    print("4. Exit")
    print("----------------------------")

    user_choice = int(input("Select an operation (1-4): "))

    previous_state = current_state

    match user_choice:

        case 1:
            action = "Suck"

            if current_state[2] == "A":
                current_state = (
                    "Clean",
                    current_state[1],
                    current_state[2]
                )
            else:
                current_state = (
                    current_state[0],
                    "Clean",
                    current_state[2]
                )

        case 2:
            action = "Move to Room 1"

            current_state = (
                current_state[0],
                current_state[1],
                "A"
            )

        case 3:
            action = "Move to Room 2"

            current_state = (
                current_state[0],
                current_state[1],
                "B"
            )

        case 4:
            print("\nExiting the program.")
            print(f"Total Operations: {step_count}")
            print(f"Final State: {current_state}")
            break

        case _:
            print("Invalid choice. Please select 1-4.")
            continue

    # Check for non-meaningful transition
    if current_state == previous_state:
        print("\nOperation produced no state change.")
        print("Transition discarded.")
        continue

    step_count += 1

    print("\n--- State Transition ---")
    print(f"Initial State  : {previous_state}")
    print(f"Action Taken   : {action}")
    print(f"Resultant State: {current_state}")
    print(f"Step           : {step_count}")

    # Check goal state
    if current_state[0] == "Clean" and current_state[1] == "Clean":
        print("\nGoal State Reached!")
        print(f"Total Operations: {step_count}")
        print(f"Final State: {current_state}")
        break

