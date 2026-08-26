# Missionaries and Cannibals Problem

## 1. Aim

To formulate and solve the classical Missionaries and Cannibals problem using state-space representation, constraint validation, state transitions, and Breadth-First Search (BFS).

Two versions are implemented:

- **V1:** Interactive state-space simulator with constraint validation.
- **V2:** Automatic BFS-based state-space solver.

---

## 2. Problem Statement

There are three missionaries and three cannibals on one side of a river. A boat is available to transport them to the opposite bank.

The boat can carry at most two people at a time.

The objective is to transport all missionaries and cannibals safely from the left bank to the right bank without ever allowing cannibals to outnumber missionaries on a bank where missionaries are present.

The problem is formulated as a state-space search problem.

---

## 3. State Representation

A state is represented as:

```text
(M_left, C_left, Boat)
```

where:

- `M_left` = number of missionaries on the left bank
- `C_left` = number of cannibals on the left bank
- `Boat` = `L` or `R`

The right-bank counts are derived as:

```text
M_right = 3 - M_left
C_right = 3 - C_left
```

### Initial State

```text
(3, 3, L)
```

### Goal State

```text
(0, 0, R)
```

---

## 4. Constraints

The following constraints must always be satisfied:

### Constraint 1: Population Bounds

```text
0 <= M_left <= 3
0 <= C_left <= 3
```

### Constraint 2: Missionary Safety

For either bank:

```text
If M > 0:
    M >= C
```

Therefore:

```text
M = 2, C = 3  → Invalid
M = 1, C = 2  → Invalid
M = 2, C = 2  → Valid
M = 0, C = 3  → Valid
```

The condition must be checked on both banks.

### Constraint 3: Boat Capacity

The boat can carry at most two people.

Valid passenger combinations are:

```text
1 Missionary
2 Missionaries
1 Cannibal
2 Cannibals
1 Missionary + 1 Cannibal
```

### Constraint 4: Boat Position

The boat can move only from the bank where it is currently located.

### Constraint 5: State Validity

Every resultant state must satisfy all constraints before it is accepted.

---

## 5. Operators

The available boat operations are:

```text
M       → 1 Missionary
MM      → 2 Missionaries
C       → 1 Cannibal
CC      → 2 Cannibals
MC      → 1 Missionary + 1 Cannibal
```

For a boat on the left bank, passengers move from left to right.

For a boat on the right bank, passengers move from right to left.

---

## 6. V1 - Interactive State-Space Simulator

V1 allows the user to manually select a boat movement.

### Workflow

```text
Current State
      ↓
User Selects Boat Move
      ↓
Generate Candidate State
      ↓
Validate Candidate State
      ↓
 ┌────┴────┐
Valid     Invalid
 ↓           ↓
Accept     Reject
 ↓
Display Transition
 ↓
Goal Test
```

### Main Components

#### State Validation

The `is_valid_state()` function checks:

- Population bounds
- Missionary safety on the left bank
- Missionary safety on the right bank

#### State Transition

A candidate state is generated based on:

- Current boat position
- Number of missionaries transported
- Number of cannibals transported

#### Transition Handling

Invalid transitions are discarded without changing the current state.

### Example

Starting from:

```text
(3, 3, L)
```

moving two cannibals produces:

```text
(3, 1, R)
```

This state is valid because:

```text
Left Bank:
3 Missionaries
1 Cannibal

Right Bank:
0 Missionaries
2 Cannibals
```

---

## 7. V2 - BFS State-Space Solver

V2 removes manual action selection and automatically searches for a solution.

Breadth-First Search is used because every boat crossing has equal cost.

The search begins at:

```text
(3, 3, L)
```

and searches for:

```text
(0, 0, R)
```

### BFS Workflow

```text
Initial State
      ↓
Generate Possible Successors
      ↓
Validate Successor States
      ↓
Discard Invalid / Visited States
      ↓
Add Valid States to Queue
      ↓
Explore Next State
      ↓
Goal Reached?
    /       \
  YES        NO
   ↓          ↓
Return      Continue
Solution    Search
```

---

## 8. BFS Algorithm

1. Define the initial state `(3, 3, L)`.
2. Define the goal state `(0, 0, R)`.
3. Insert the initial state into a queue.
4. Mark the initial state as visited.
5. Remove the next state from the queue.
6. Check whether it is the goal state.
7. Generate all possible boat movements.
8. Generate the resulting states.
9. Validate each resulting state.
10. Ignore invalid states.
11. Ignore states that have already been visited.
12. Add new valid states to the queue.
13. Store the action and resulting state as part of the solution path.
14. Repeat until the goal is found or the queue becomes empty.
15. Display the solution path and search statistics.

---

## 9. Why BFS?

The problem can be represented as an unweighted graph:

```text
State = Node
Boat Crossing = Edge
```

Each crossing has the same cost.

Therefore, BFS explores the state space level by level and guarantees the shortest solution in terms of number of crossings.

For the classic problem:

```text
Initial State → Goal State
```

the BFS solution requires:

```text
11 crossings
```

---

## 10. State-Space Representation

The state space consists of valid combinations of:

```text
Missionaries on Left
Cannibals on Left
Boat Position
```

The complete state-space / transition diagram is provided in:

```text
outputs/diagrams/missionaries_and_cannibals_state_space.png
```

The diagram highlights valid transitions from the initial state toward the goal while respecting the missionary-safety constraint.

---

## 11. Example Solution

The BFS solver should find a shortest solution of 11 crossings.

A typical solution path is represented as:

```text
Step 0: (3, 3, L)

Step 1: 2 Cannibals
         ↓
         (3, 1, R)

Step 2: 1 Cannibal
         ↓
         (3, 2, L)

Step 3: 2 Cannibals
         ↓
         (3, 0, R)

Step 4: 1 Cannibal
         ↓
         (3, 1, L)

Step 5: 2 Missionaries
         ↓
         (1, 1, R)

Step 6: 1 Missionary + 1 Cannibal
         ↓
         (2, 2, L)

Step 7: 2 Missionaries
         ↓
         (0, 2, R)

Step 8: 1 Cannibal
         ↓
         (0, 3, L)

Step 9: 2 Cannibals
         ↓
         (0, 1, R)

Step 10: 1 Missionary
          ↓
          (1, 1, L)

Step 11: 1 Missionary + 1 Cannibal
          ↓
          (0, 0, R)
```

Each state satisfies the constraints.

---

## 12. V1 vs V2

| Aspect | V1 | V2 |
|---|---|---|
| Action selection | User | BFS solver |
| State representation | Same | Same |
| Constraint validation | Yes | Yes |
| State transition | Manual | Automatic |
| Search | None | BFS |
| Solution generation | User-dependent | Automatic |
| Shortest solution | Not guaranteed | Guaranteed |
| Goal testing | Yes | Yes |
| Main concept | State-space formulation | State-space search |

The main conceptual upgrade is:

```text
V1:
Human chooses a valid transition

V2:
Algorithm explores valid transitions to find the goal
```

---

## 13. Results

The Missionaries and Cannibals problem was successfully implemented as a constrained state-space problem.

### V1

- State representation was implemented.
- Boat movements were represented as operators.
- Candidate states were generated.
- Invalid states were rejected.
- Missionary safety was checked on both banks.
- Goal testing was implemented.
- Interactive state transitions were displayed.

### V2

- Valid successor states were generated automatically.
- Invalid and previously visited states were discarded.
- BFS explored the state space systematically.
- A solution path was generated automatically.
- The shortest solution was found in **11 crossings**.
- The final state was `(0, 0, R)`.

---

## 14. Performance Analysis

This is a small state-space search problem, so the most useful measures are search-related rather than ML classification metrics.

Relevant measures include:

- Number of states explored
- Number of valid states generated
- Number of solution steps
- Number of visited states
- Whether the goal was reached
- Search strategy used

For the classic configuration:

```text
Initial State : (3, 3, L)
Goal State    : (0, 0, R)
Search        : BFS
Solution      : 11 crossings
Goal Reached  : YES
```

Because BFS explores states level by level, the first solution found is optimal with respect to the number of crossings.

---

## 15. Observations

1. A complete state must include the boat position in addition to the numbers of missionaries and cannibals.
2. A state can be syntactically valid but logically unsafe.
3. Both banks must be checked for missionary safety.
4. Invalid states should never be added to the search space.
5. The same state can be reached through different sequences, so visited-state tracking is necessary.
6. V1 demonstrates state formulation and constraint handling.
7. V2 demonstrates automatic state-space exploration.
8. BFS provides a systematic search strategy.
9. BFS finds the shortest solution when all actions have equal cost.
10. The problem demonstrates how constraints reduce the effective search space.

---

## 16. Learning Outcomes

After completing this experiment, the following concepts were understood and implemented:

- State-space representation
- Initial and goal states
- State transitions
- Operators
- Constraint validation
- Valid and invalid states
- Missionary-safety condition
- Successor-state generation
- Visited-state tracking
- Breadth-First Search
- Shortest-path reasoning
- Goal testing
- State-space exploration

---

## 17. Output Artifacts

```text
outputs/
├── screenshots/
│   ├── v1_valid_transition.png
│   ├── v1_invalid_transition.png
│   └── v2_bfs_solution.png
│
└── diagrams/
    └── missionaries_and_cannibals_state_space.png
```

---

## 18. Conclusion

The Missionaries and Cannibals problem was successfully formulated and solved as a constrained state-space problem.

V1 demonstrated manual state transitions and constraint validation. V2 extended the implementation with Breadth-First Search, allowing the system to automatically explore valid states and find a shortest solution.

The experiment combines state representation, constraints, successor generation, visited-state tracking, goal testing, and systematic search, providing a strong conclusion to the Unit 1 state-space experiments.
