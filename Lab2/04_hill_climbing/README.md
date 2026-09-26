# Hill Climbing Search

## Aim

To implement the Hill Climbing search algorithm in Python and find the maximum value of a mathematical function by iteratively moving toward a better neighboring state.

---

## Problem Statement

Implement the Hill Climbing algorithm to maximize the function:

f(x) = -(x - 5)^2 + 25

The algorithm starts from a user-defined state and repeatedly moves to a neighboring state with a higher function value until no better neighboring state exists.

---

## Algorithm

1. Take the starting value from the user.
2. Set the starting value as the current state.
3. Calculate the function value of the current state.
4. Generate the left and right neighboring states.
5. Calculate the function values of both neighbors.
6. Compare the neighboring values with the current value.
7. Move to the neighbor having a higher value.
8. Repeat the process until neither neighbor has a higher value.
9. Stop when a local maximum is reached.
10. Display the best state and its function value.

---

## Function Used

The function used in this experiment is:

f(x) = -(x - 5)^2 + 25

The maximum value occurs at:

- **State:** `x = 5`
- **Maximum value:** `f(5) = 25`

---

## Implementation

The implementation uses a simple iterative approach.

- No external libraries are required.
- The current state is compared with its immediate left and right neighbors.
- The algorithm moves only when a better neighboring state is found.
- The search terminates when no better neighbor exists.

### Search Flow

```text
Current State
      |
      v
Evaluate Current
      |
      v
Evaluate Left & Right Neighbors
      |
      v
Is a Neighbor Better?
    /        \
  Yes         No
   |           |
   v           v
Move to      Stop
Better       at Local
Neighbor     Maximum
```

---

## Test Cases

### Test Case 1

**Starting value:** `1`

Search progression:

```text
1 → 2 → 3 → 4 → 5
```

Result:

```text
Best state: 5
Best value: 25
```

### Test Case 2

**Starting value:** `3`

Search progression:

```text
3 → 4 → 5
```

Result:

```text
Best state: 5
Best value: 25
```

### Test Case 3

**Starting value:** `5`

Search progression:

```text
5
```

Result:

```text
Best state: 5
Best value: 25
```

The algorithm stops immediately because neither neighboring state provides a better value.

### Test Case 4

**Starting value:** `8`

Search progression:

```text
8 → 7 → 6 → 5
```

Result:

```text
Best state: 5
Best value: 25
```

---

## Output Screenshots

### Starting from 1

![Hill Climbing from 1](outputs/hill_climbing_start_1.png)

### Starting from 3

![Hill Climbing from 3](outputs/hill_climbing_start_3.png)

### Starting from 5

![Hill Climbing from 5](outputs/hill_climbing_start_5.png)

### Starting from 8

![Hill Climbing from 8](outputs/hill_climbing_start_8.png)

---

## Performance Analysis

Let `n` represent the number of states explored during the search.

### Time Complexity

Each iteration evaluates the current state and its two neighboring states. The work per iteration is constant:

O(1)

For `n` iterations:

O(n)

### Space Complexity

The algorithm stores only the current state and a constant number of neighboring states:

O(1)

---

## Characteristics

| Property | Description |
|---|---|
| Search Type | Local Search |
| Strategy | Greedy Improvement |
| Direction | Toward a better neighboring state |
| Memory Usage | Low |
| Complete | No |
| Optimal | No in the general case |
| External Libraries | None |

---

## Limitations

Hill Climbing can get stuck at:

- Local maxima
- Plateaus
- Ridges

Therefore, reaching a state where no better neighbor exists does not necessarily mean that the global optimum has been found.

In this experiment, the selected function has its maximum at `x = 5`, so all tested starting points successfully reach the maximum.

---

## Learning Outcomes

After completing this experiment, the following concepts were understood:

1. Working principle of Hill Climbing search.
2. Representation of states and neighboring states.
3. Greedy movement toward a better state.
4. Local search and optimization.
5. Difference between local maximum and global maximum.
6. Time and space complexity of a simple Hill Climbing implementation.
7. Limitations of Hill Climbing search.
