def fill_jug1(jug1_capacity, current_state):
    return (jug1_capacity, current_state[1])


def fill_jug2(jug2_capacity, current_state):
    return (current_state[0], jug2_capacity)


def empty_jug1(current_state):
    return (0, current_state[1])


def empty_jug2(current_state):
    return (current_state[0], 0)


def pour_jug1_to_jug2(jug2_capacity, current_state):
    pour_amount = min(
        current_state[0],
        jug2_capacity - current_state[1]
    )

    return (
        current_state[0] - pour_amount,
        current_state[1] + pour_amount
    )


def pour_jug2_to_jug1(jug1_capacity, current_state):
    pour_amount = min(
        current_state[1],
        jug1_capacity - current_state[0]
    )

    return (
        current_state[0] + pour_amount,
        current_state[1] - pour_amount
    )


def generate_next_states(
    jug1_capacity,
    jug2_capacity,
    current_state,
    visited_states
):
    possible_transitions = [
        (
            "Fill Jug 1",
            fill_jug1(jug1_capacity, current_state)
        ),
        (
            "Fill Jug 2",
            fill_jug2(jug2_capacity, current_state)
        ),
        (
            "Empty Jug 1",
            empty_jug1(current_state)
        ),
        (
            "Empty Jug 2",
            empty_jug2(current_state)
        ),
        (
            "Pour Jug 1 → Jug 2",
            pour_jug1_to_jug2(jug2_capacity, current_state)
        ),
        (
            "Pour Jug 2 → Jug 1",
            pour_jug2_to_jug1(jug1_capacity, current_state)
        )
    ]

    next_states = []

    for action, resultant_state in possible_transitions:

        if resultant_state == current_state:
            continue

        if resultant_state in visited_states:
            continue

        next_states.append(
            (current_state, action, resultant_state)
        )

    return next_states


jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target amount of water to be measured: "))

current_state = (0, 0)
visited_states = {current_state}

print(f"\nInitial State: {current_state}")
print(f"Target Amount: {target_amount} liters")

while True:

    print("\n========== CURRENT STATE ==========")
    print(f"State: {current_state}")

    next_states = generate_next_states(
        jug1_capacity,
        jug2_capacity,
        current_state,
        visited_states
    )

    if not next_states:
        print("\nNo new states can be generated.")
        break

    print("\n--- Possible Transitions ---")

    for index, transition in enumerate(next_states, start=1):

        initial_state, action, resultant_state = transition

        print(f"\n{index}.")
        print(f"Initial State   : {initial_state}")
        print(f"Action Taken    : {action}")
        print(f"Resultant State : {resultant_state}")

    print("\n0. Exit")

    user_choice = int(
        input("\nSelect a transition: ")
    )

    if user_choice == 0:
        print("\nExiting the program.")
        break

    if user_choice < 1 or user_choice > len(next_states):
        print("\nInvalid choice.")
        continue

    selected_transition = next_states[user_choice - 1]

    initial_state, action, resultant_state = selected_transition

    current_state = resultant_state
    visited_states.add(current_state)

    print("\n--- Transition Selected ---")
    print(f"Initial State   : {initial_state}")
    print(f"Action Taken    : {action}")
    print(f"Resultant State : {resultant_state}")

    if (
        current_state[0] == target_amount
        or current_state[1] == target_amount
    ):
        print(
            f"\nTarget amount of {target_amount} liters reached!"
        )
        break


print("\n========== SUMMARY ==========")
print(f"Visited States: {len(visited_states)}")
print(f"Final State   : {current_state}")