jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target amount of water to be measured: "))

current_state = (0, 0)
step_count = 0

print(f"\nInitial State: {current_state}")
print(f"Target Amount: {target_amount} liters")

while True:

    print("\n--- Available Operations ---")
    print("1. Fill Jug 1")
    print("2. Fill Jug 2")
    print("3. Empty Jug 1")
    print("4. Empty Jug 2")
    print("5. Pour Jug 1 → Jug 2")
    print("6. Pour Jug 2 → Jug 1")
    print("7. Exit")
    print("----------------------------")

    user_choice = int(input("Select an operation (1-7): "))

    previous_state = current_state

    match user_choice:

        case 1:
            action = "Fill Jug 1"
            current_state = (jug1_capacity, current_state[1])

        case 2:
            action = "Fill Jug 2"
            current_state = (current_state[0], jug2_capacity)

        case 3:
            action = "Empty Jug 1"
            current_state = (0, current_state[1])

        case 4:
            action = "Empty Jug 2"
            current_state = (current_state[0], 0)

        case 5:
            action = "Pour Jug 1 → Jug 2"

            pour_amount = min(
                current_state[0],
                jug2_capacity - current_state[1]
            )

            current_state = (
                current_state[0] - pour_amount,
                current_state[1] + pour_amount
            )

        case 6:
            action = "Pour Jug 2 → Jug 1"

            pour_amount = min(
                current_state[1],
                jug1_capacity - current_state[0]
            )

            current_state = (
                current_state[0] + pour_amount,
                current_state[1] - pour_amount
            )

        case 7:
            print("\nExiting the program.")
            print(f"Total Operations: {step_count}")
            print(f"Final State: {current_state}")
            break

        case _:
            print("Invalid choice. Please select 1-7.")
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