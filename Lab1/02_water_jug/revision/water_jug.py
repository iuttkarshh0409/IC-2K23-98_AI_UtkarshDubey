capacity_A=int(input("Enter capacity permitted for Jug A: "))
capacity_B=int(input("Enter capacity permitted for Jug B: "))
target_capacity=int(input("Enter capacity to be measured: "))

current_state= (0,0)
step_count=0

print("Initial State: ", current_state)
print("Target capacity: ", target_capacity)

while True:

    print("\n--- Available Operations ---")
    print("1. Fill Jug A")
    print("2. Fill Jug B")
    print("3. Empty Jug A")
    print("4. Empty Jug B")
    print("5. Pour Jug A → Jug B")
    print("6. Pour Jug B → Jug A")
    print("7. Exit")
    print("----------------------------")

    user_choice = int(input("Select an operation (1-7): "))

    previous_state = current_state

    match user_choice:

        case 1:
            action = "Fill Jug A"
            current_state = (capacity_A, current_state[1])

        case 2:
            action = "Fill Jug B"
            current_state = (current_state[0], capacity_B)

        case 3:
            action = "Empty Jug A"
            current_state = (0, current_state[1])

        case 4:
            action = "Empty Jug B"
            current_state = (current_state[0], 0)

        case 5:
            action = "Pour Jug A → Jug B"

            pour_amount = min(
                current_state[0],
                capacity_B - current_state[1]
            )

            current_state = (
                current_state[0] - pour_amount,
                current_state[1] + pour_amount
            )

        case 6:
            action = "Pour Jug B → Jug A"

            pour_amount = min(
                current_state[1],
                capacity_A - current_state[0]
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

    if current_state[0] == target_capacity or current_state[1] == target_capacity:
        print(f"\nTarget capacity {target_capacity} L achieved!")
        break
