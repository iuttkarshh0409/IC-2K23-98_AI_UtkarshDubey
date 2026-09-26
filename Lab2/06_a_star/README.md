# A* Search

## Aim

To implement the A* search algorithm in Python using the evaluation function `f(n) = g(n) + h(n)` to find a goal node with minimum path cost.

---

## Problem Statement

Implement the A* search algorithm to find a path from a starting node to a goal node in a weighted graph.

The algorithm should consider:

- `g(n)` — actual cost from the starting node to the current node.
- `h(n)` — estimated cost from the current node to the goal.
- `f(n)` — estimated total cost through the current node.

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

---

## Graph Used

The graph used in this experiment is:

```text
        A
       / \
      B   C
     / \   \
    D   E   F
         \
          F
```

Edges and their costs:

| Edge | Cost |
|---|---:|
| A → B | 1 |
| A → C | 4 |
| B → D | 5 |
| B → E | 2 |
| C → F | 3 |
| E → F | 1 |

---

## Heuristic Values

The heuristic values used are:

| Node | h(n) |
|---|---:|
| A | 5 |
| B | 3 |
| C | 3 |
| D | 6 |
| E | 1 |
| F | 0 |

The goal node `F` has a heuristic value of `0`.

---

## Algorithm

1. Define the weighted graph.
2. Define the heuristic value for each node.
3. Take the starting node and goal node as input.
4. Validate the input nodes.
5. Add the starting node to the OPEN list.
6. Set the starting node's `g` value to `0`.
7. While the OPEN list is not empty:
   - Select the node with the smallest `f(n)`.
   - Calculate `f(n)` using `g(n) + h(n)`.
   - Remove the selected node from the OPEN list.
   - Add it to the VISITED list.
   - If it is the goal node, terminate successfully.
   - For every neighboring node:
     - Calculate the new path cost.
     - Update `g(n)` if the new path is cheaper.
     - Add the neighbor to the OPEN list if required.
8. If the OPEN list becomes empty before reaching the goal, report search failure.

---

## Pseudocode

```text
START

Define graph
Define edge costs
Define heuristic values

Input starting node
Input goal node

If starting node or goal node is invalid:
    Display invalid input
    STOP

OPEN = [starting node]
VISITED = []

Set g(start) = 0

WHILE OPEN is not empty:

    Select node from OPEN
    having the smallest:

        f(n) = g(n) + h(n)

    Remove selected node from OPEN

    If node is already visited:
        Continue

    Add node to VISITED
    Display node and its g, h and f values

    If node is the goal:
        Display search successful
        Display total cost
        STOP

    For each neighbour:

        Calculate:

        new_g = g(current) + cost(current, neighbour)

        If neighbour has no previous g value
        OR new_g is smaller than its previous g value:

            Update g(neighbour)

            If neighbour is not visited
            and not already in OPEN:

                Add neighbour to OPEN

If OPEN becomes empty:

    Display search failure

END
```

---

## Evaluation Function

A* uses:

```text
f(n) = g(n) + h(n)
```

where:

```text
g(n) = actual cost from start to n
h(n) = estimated cost from n to goal
f(n) = estimated total cost
```

For example, after reaching node `E`:

```text
g(E) = 3
h(E) = 1

f(E) = 3 + 1
     = 4
```

The node with the smallest `f(n)` is selected next.

---

## Example Execution

For:

```text
Starting node: A
Goal node: F
```

The search proceeds as:

```text
A → B → E → F
```

### Step 1: Node A

```text
g(A) = 0
h(A) = 5
f(A) = 5
```

From A:

```text
g(B) = 0 + 1 = 1
f(B) = 1 + 3 = 4

g(C) = 0 + 4 = 4
f(C) = 4 + 3 = 7
```

Therefore, B is selected.

### Step 2: Node B

```text
g(B) = 1
h(B) = 3
f(B) = 4
```

From B:

```text
g(D) = 1 + 5 = 6
f(D) = 6 + 6 = 12

g(E) = 1 + 2 = 3
f(E) = 3 + 1 = 4
```

Therefore, E is selected.

### Step 3: Node E

```text
g(E) = 3
h(E) = 1
f(E) = 4
```

From E:

```text
g(F) = 3 + 1 = 4
f(F) = 4 + 0 = 4
```

F is the goal.

### Final Result

```text
A → B → E → F
```

Total path cost:

```text
1 + 2 + 1 = 4
```

---

## Test Cases

### Test Case 1: Successful Search

**Start:** `A`  
**Goal:** `F`

Expected traversal:

```text
A → B → E → F
```

Expected total cost:

```text
4
```

---

### Test Case 2: Start and Goal Are Same

**Start:** `A`  
**Goal:** `A`

Expected traversal:

```text
A
```

Expected total cost:

```text
0
```

---

### Test Case 3: Search from B to F

**Start:** `B`  
**Goal:** `F`

The expected path is:

```text
B → E → F
```

Expected total cost:

```text
3
```

---

### Test Case 4: Invalid Input

**Start:** `X`  
**Goal:** `F`

Expected result:

```text
Invalid starting or goal node.
```

---

## Output Screenshots

### A* Search: A to F

![A* Search A to F](outputs/a_star_A_to_F.png)

### A* Search: B to F

![A* Search B to F](outputs/a_star_B_to_F.png)

### Invalid Input

![Invalid Input](outputs/invalid_input.png)

---

## Performance Analysis

Let `V` be the number of vertices and `E` be the number of edges.

The current V1 implementation uses Python lists and scans the OPEN list to find the node with the smallest `f(n)`.

### Time Complexity

Finding the minimum `f(n)` from the OPEN list can take:

```text
O(V)
```

In the worst case, the overall implementation can take:

```text
O(V²)
```

because a linear scan is performed repeatedly.

### Space Complexity

The OPEN list, VISITED list, and `g_score` dictionary can store information for up to `V` nodes.

Therefore:

```text
O(V)
```

---

## Characteristics

| Property | Description |
|---|---|
| Search Type | Informed Search |
| Strategy | Cost + Heuristic |
| Evaluation Function | `f(n) = g(n) + h(n)` |
| Data Structure | Python List |
| Uses Edge Costs | Yes |
| Uses Heuristic | Yes |
| Complete | Yes under standard conditions |
| Optimal | Yes with an admissible heuristic |
| Memory Usage | O(V) for this implementation |
| External Libraries | None |

---

## Difference Between Best First Search and A*

| Feature | Best First Search | A* |
|---|---|---|
| Evaluation | `h(n)` | `g(n) + h(n)` |
| Actual path cost | Not considered | Considered |
| Heuristic | Used | Used |
| Shortest path | Not guaranteed | Guaranteed under appropriate heuristic conditions |
| Search behavior | Greedy | Cost-aware and heuristic-guided |

---

## Limitations

The performance and correctness of A* depend on the heuristic and implementation.

- A poor heuristic can cause unnecessary exploration.
- A* can require significant memory for large search spaces.
- The current V1 uses a simple list instead of a priority queue, making minimum-node selection less efficient.
- Optimality depends on appropriate heuristic conditions.

---

## Learning Outcomes

After completing this experiment, the following concepts were understood:

1. Working principle of A* search.
2. Difference between `g(n)`, `h(n)`, and `f(n)`.
3. Use of actual path cost in informed search.
4. Use of heuristic functions.
5. Selection of nodes using `f(n) = g(n) + h(n)`.
6. Updating path costs when a cheaper route is found.
7. Difference between Best First Search and A*.
8. Time and space complexity of a list-based A* implementation.
