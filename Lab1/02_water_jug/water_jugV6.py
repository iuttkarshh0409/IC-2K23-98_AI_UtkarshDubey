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
    current_state
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

        next_states.append(
            (action, resultant_state)
        )

    return next_states


jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target amount of water to be measured: "))

initial_state = (0, 0)

# Each item contains:
# (current_state, path_taken)
pending_states = [
    (initial_state, [])
]

visited_states = {initial_state}

solution_path = None

while pending_states:

    current_state, path_taken = pending_states.pop(0)

    print(f"\nExploring State: {current_state}")

    # Check whether target has been reached
    if (
        current_state[0] == target_amount
        or current_state[1] == target_amount
    ):
        solution_path = path_taken
        break

    next_states = generate_next_states(
        jug1_capacity,
        jug2_capacity,
        current_state
    )

    for action, resultant_state in next_states:

        if resultant_state in visited_states:
            continue

        visited_states.add(resultant_state)

        new_path = path_taken + [
            (current_state, action, resultant_state)
        ]

        pending_states.append(
            (resultant_state, new_path)
        )


print("\n========== SEARCH RESULT ==========")

if solution_path is not None:

    for step, transition in enumerate(
        solution_path,
        start=1
    ):

        initial_state, action, resultant_state = transition

        print(f"\nStep {step}")
        print(f"Initial State   : {initial_state}")
        print(f"Action Taken    : {action}")
        print(f"Resultant State : {resultant_state}")

    print("\n===================================")
    print(f"Total Operations : {len(solution_path)}")
    print(f"Visited States   : {len(visited_states)}")

    final_state = solution_path[-1][2]
    print(f"Final State      : {final_state}")

else:

    print("No solution exists for the given configuration.")
    print(f"Visited States: {len(visited_states)}")