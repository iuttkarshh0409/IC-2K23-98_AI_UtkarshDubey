# Vacuum Cleaner V2
# State-Based Intelligent Agent


current_state = ("Dirty", "Dirty", "A")
step_count = 0

print("\n========== VACUUM CLEANER V2 ==========")
print(f"Initial State: {current_state}")
print("Goal: Both rooms must be Clean")
print("========================================")


while True:

    # --------------------------------------------------
    # Goal Test
    # --------------------------------------------------

    if current_state[0] == "Clean" and current_state[1] == "Clean":
        print("\nGoal State Reached!")
        print(f"Total Operations: {step_count}")
        print(f"Final State: {current_state}")
        break


    previous_state = current_state

    # --------------------------------------------------
    # Agent Decision
    # --------------------------------------------------

    vacuum_position = current_state[2]

    if vacuum_position == "A":

        # Rule 2:
        # Vacuum can only clean the room it is currently in.
        if current_state[0] == "Dirty":

            action = "Suck Room 1"

            current_state = (
                "Clean",
                current_state[1],
                current_state[2]
            )

        # Current room is already clean.
        # Move to the other room.
        else:

            action = "Move to Room 2"

            current_state = (
                current_state[0],
                current_state[1],
                "B"
            )

    else:

        # Vacuum is in Room 2.
        if current_state[1] == "Dirty":

            action = "Suck Room 2"

            current_state = (
                current_state[0],
                "Clean",
                current_state[2]
            )

        # Current room is already clean.
        # Move to the other room.
        else:

            action = "Move to Room 1"

            current_state = (
                current_state[0],
                current_state[1],
                "A"
            )


    # --------------------------------------------------
    # Check for Non-Meaningful Transition
    # --------------------------------------------------

    if current_state == previous_state:

        print("\nOperation produced no state change.")
        print("Transition discarded.")
        continue


    # --------------------------------------------------
    # Record Transition
    # --------------------------------------------------

    step_count += 1

    print("\n--- State Transition ---")
    print(f"Initial State  : {previous_state}")
    print(f"Action Taken   : {action}")
    print(f"Resultant State: {current_state}")
    print(f"Step           : {step_count}")