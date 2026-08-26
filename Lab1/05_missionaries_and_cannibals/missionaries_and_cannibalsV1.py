# Missionaries and Cannibals V1
# Interactive State-Space Simulator


TOTAL_MISSIONARIES = 3
TOTAL_CANNIBALS = 3
BOAT_CAPACITY = 2

current_state = (3, 3, "L")
step_count = 0


# --------------------------------------------------
# State Validation
# --------------------------------------------------

def is_valid_state(state):

    missionaries_left, cannibals_left, boat = state

    missionaries_right = TOTAL_MISSIONARIES - missionaries_left
    cannibals_right = TOTAL_CANNIBALS - cannibals_left

    # Check whether the number of people is valid
    if not (
        0 <= missionaries_left <= TOTAL_MISSIONARIES
        and 0 <= cannibals_left <= TOTAL_CANNIBALS
    ):
        return False

    # Check left bank
    if (
        missionaries_left > 0
        and missionaries_left < cannibals_left
    ):
        return False

    # Check right bank
    if (
        missionaries_right > 0
        and missionaries_right < cannibals_right
    ):
        return False

    return True


# --------------------------------------------------
# Display State
# --------------------------------------------------

def display_state(state):

    missionaries_left, cannibals_left, boat = state

    missionaries_right = TOTAL_MISSIONARIES - missionaries_left
    cannibals_right = TOTAL_CANNIBALS - cannibals_left

    print(
        f"\nLeft Bank  : M = {missionaries_left}, "
        f"C = {cannibals_left}"
    )

    print(
        f"Right Bank : M = {missionaries_right}, "
        f"C = {cannibals_right}"
    )

    print(f"Boat       : {'Left' if boat == 'L' else 'Right'}")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

print("\n========== MISSIONARIES & CANNIBALS V1 ==========")

print("\nInitial State:")
display_state(current_state)

print("\nGoal State:")
print("Left Bank  : M = 0, C = 0")
print("Right Bank : M = 3, C = 3")
print("Boat       : Right")


while True:

    # --------------------------------------------------
    # Goal Test
    # --------------------------------------------------

    if current_state == (0, 0, "R"):

        print("\n========== GOAL REACHED ==========")
        print(f"Total Operations: {step_count}")
        display_state(current_state)
        break


    # --------------------------------------------------
    # Available Boat Moves
    # --------------------------------------------------

    print("\n--- Available Boat Moves ---")
    print("1. 1 Missionary")
    print("2. 2 Missionaries")
    print("3. 1 Cannibal")
    print("4. 2 Cannibals")
    print("5. 1 Missionary + 1 Cannibal")
    print("6. Exit")
    print("----------------------------")

    user_choice = int(input("Select a move (1-6): "))

    previous_state = current_state


    # --------------------------------------------------
    # Determine Passenger Combination
    # --------------------------------------------------

    match user_choice:

        case 1:
            missionaries = 1
            cannibals = 0
            action = "1 Missionary"

        case 2:
            missionaries = 2
            cannibals = 0
            action = "2 Missionaries"

        case 3:
            missionaries = 0
            cannibals = 1
            action = "1 Cannibal"

        case 4:
            missionaries = 0
            cannibals = 2
            action = "2 Cannibals"

        case 5:
            missionaries = 1
            cannibals = 1
            action = "1 Missionary + 1 Cannibal"

        case 6:
            print("\nExiting the program.")
            print(f"Total Operations: {step_count}")
            display_state(current_state)
            break

        case _:
            print("Invalid choice. Please select 1-6.")
            continue


    # --------------------------------------------------
    # Generate Candidate State
    # --------------------------------------------------

    missionaries_left, cannibals_left, boat = current_state

    if boat == "L":

        new_state = (
            missionaries_left - missionaries,
            cannibals_left - cannibals,
            "R"
        )

    else:

        new_state = (
            missionaries_left + missionaries,
            cannibals_left + cannibals,
            "L"
        )


    # --------------------------------------------------
    # Validate Transition
    # --------------------------------------------------

    if not is_valid_state(new_state):

        print("\nInvalid transition.")
        print("The resulting state violates the constraints.")
        print("Transition discarded.")
        continue


    # --------------------------------------------------
    # Record Valid Transition
    # --------------------------------------------------

    current_state = new_state
    step_count += 1

    print("\n--- State Transition ---")
    print(f"Initial State  : {previous_state}")
    print(f"Action Taken   : {action}")
    print(f"Resultant State: {current_state}")
    print(f"Step           : {step_count}")

    display_state(current_state)