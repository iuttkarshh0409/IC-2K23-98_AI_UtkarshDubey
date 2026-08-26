# Missionaries and Cannibals V2
# BFS State-Space Solver


from collections import deque


TOTAL_MISSIONARIES = 3
TOTAL_CANNIBALS = 3


# --------------------------------------------------
# State Validation
# --------------------------------------------------

def is_valid_state(state):

    missionaries_left, cannibals_left, boat = state

    missionaries_right = TOTAL_MISSIONARIES - missionaries_left
    cannibals_right = TOTAL_CANNIBALS - cannibals_left

    # Check population bounds
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
# Generate Valid Successor States
# --------------------------------------------------

def generate_successors(state):

    missionaries_left, cannibals_left, boat = state

    possible_moves = [
        (1, 0, "1 Missionary"),
        (2, 0, "2 Missionaries"),
        (0, 1, "1 Cannibal"),
        (0, 2, "2 Cannibals"),
        (1, 1, "1 Missionary + 1 Cannibal")
    ]

    successors = []

    for missionaries, cannibals, action in possible_moves:

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

        if is_valid_state(new_state):

            successors.append(
                (new_state, action)
            )

    return successors


# --------------------------------------------------
# Breadth-First Search
# --------------------------------------------------

def bfs(start_state, goal_state):

    queue = deque()

    # Store:
    # (current_state, path)
    queue.append(
        (start_state, [])
    )

    visited = {start_state}

    explored_states = []

    while queue:

        current_state, path = queue.popleft()

        explored_states.append(current_state)

        # Goal test
        if current_state == goal_state:
            return path, explored_states

        for next_state, action in generate_successors(current_state):

            if next_state not in visited:

                visited.add(next_state)

                new_path = path + [
                    (action, next_state)
                ]

                queue.append(
                    (next_state, new_path)
                )

    return None, explored_states


# --------------------------------------------------
# Main Program
# --------------------------------------------------

start_state = (3, 3, "L")
goal_state = (0, 0, "R")


print("\n========== MISSIONARIES & CANNIBALS V2 ==========")

print(f"Initial State: {start_state}")
print(f"Goal State   : {goal_state}")

print("\nSearching state space using BFS...")


solution, explored_states = bfs(
    start_state,
    goal_state
)


# --------------------------------------------------
# Display Search Result
# --------------------------------------------------

if solution is None:

    print("\nNo solution exists.")

else:

    print("\n========== SOLUTION FOUND ==========")

    current_state = start_state

    print(f"\nStep 0")
    print(f"State  : {current_state}")

    for step, (action, next_state) in enumerate(
        solution,
        start=1
    ):

        print(f"\nStep {step}")
        print(f"Action : {action}")
        print(f"State  : {next_state}")

        current_state = next_state


    print("\n========== SEARCH ANALYSIS ==========")

    print(f"States Explored : {len(explored_states)}")
    print(f"Solution Steps  : {len(solution)}")
    print(f"Final State     : {current_state}")

    print("\nGoal Reached: YES")

print("\n====================================")