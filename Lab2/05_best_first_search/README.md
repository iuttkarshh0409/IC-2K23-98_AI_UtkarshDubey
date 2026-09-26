# Best First Search

## Aim

To implement the Best First Search algorithm in Python using heuristic values to select the most promising node during the search.

---

## Problem Statement

Implement Best First Search to find a goal node in a graph.

The algorithm should use a heuristic function `h(n)` to select the node with the smallest heuristic value from the currently available nodes.

---

## Graph Used

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

Graph representation:

```text
A → B, C
B → D, E
C → F
D → None
E → None
F → None
```

---

## Heuristic Values

| Node | h(n) |
|---|---:|
| A | 6 |
| B | 4 |
| C | 2 |
| D | 7 |
| E | 3 |
| F | 0 |

A smaller heuristic value indicates that the node is considered more promising. The goal node `F` has a heuristic value of `0`.

---

## Algorithm

1. Define the graph.
2. Define the heuristic value for each node.
3. Take the starting node and goal node as input.
4. Validate the input nodes.
5. Add the starting node to the OPEN list.
6. Repeat while the OPEN list is not empty:
   - Select the node with the smallest heuristic value.
   - Remove the selected node from the OPEN list.
   - Add it to the VISITED list.
   - Check whether it is the goal node.
   - If it is the goal, terminate the search successfully.
   - Otherwise, add its unvisited neighbors to the OPEN list.
7. If the OPEN list becomes empty before reaching the goal, report search failure.

---

## Pseudocode

```text
START

Define graph
Define heuristic values

Input starting node
Input goal node

If starting node or goal node is invalid:
    Display invalid input
    STOP

OPEN = [starting node]
VISITED = []

WHILE OPEN is not empty:

    Select node with minimum heuristic value

    Remove selected node from OPEN

    If node is not visited:

        Add node to VISITED
        Display node

        If node is goal:
            Display search successful
            STOP

        For each neighbour of node:
            If neighbour is not visited
            and neighbour is not in OPEN:
                Add neighbour to OPEN

Display search failure if goal is not reached

END
```

---

## Implementation

The implementation uses:

- Python dictionaries for graph and heuristic representation.
- Python lists for the OPEN and VISITED lists.
- A simple linear search to find the node with the minimum heuristic value.
- No external libraries.

### Core Selection Logic

```python
best_node = open_list[0]

for node in open_list:
    if heuristic[node] < heuristic[best_node]:
        best_node = node
```

This makes the search heuristic-driven.

---

## Example Execution

For:

```text
Starting node: A
Goal node: F
```

The search proceeds as:

```text
A
↓
B, C
↓
C
↓
F
```

Heuristic comparison:

```text
h(B) = 4
h(C) = 2
```

Therefore, `C` is selected before `B`.

After expanding `C`:

```text
h(B) = 4
h(F) = 0
```

Therefore, `F` is selected and the goal is reached.

Expected traversal:

```text
A → C → F
```

---

## Test Cases

### Test Case 1: Successful Search

**Start:** `A`  
**Goal:** `F`

Expected traversal:

```text
A → C → F
```

Result:

```text
Goal reached!
```

### Test Case 2: Search for E

**Start:** `A`  
**Goal:** `E`

Expected traversal:

```text
A → C → B → E
```

Result:

```text
Goal reached!
```

### Test Case 3: Search from B to E

**Start:** `B`  
**Goal:** `E`

Expected traversal:

```text
B → E
```

Result:

```text
Goal reached!
```

### Test Case 4: Start and Goal Are Same

**Start:** `A`  
**Goal:** `A`

Expected traversal:

```text
A
```

Result:

```text
Goal reached!
```

### Test Case 5: Invalid Input

**Start:** `X`  
**Goal:** `F`

Result:

```text
Invalid starting or goal node.
```

---

## Output Screenshots

### Best First Search: A to F

![Best First Search A to F](outputs/best_first_search_A_to_F.png)

### Best First Search: A to E

![Best First Search A to E](outputs/best_first_search_A_to_E.png)

### Invalid Input

![Invalid Input](outputs/invalid_input.png)

---

## Performance Analysis

Let `V` be the number of nodes and `E` be the number of edges.

### Time Complexity

The V1 implementation uses a list and scans the OPEN list to find the node with the minimum heuristic value.

Selecting the best node can take:

```text
O(V)
```

In the worst case, the overall search can take:

```text
O(V²)
```

for this simple list-based implementation.

### Space Complexity

The OPEN and VISITED lists can store up to the number of nodes in the graph.

Therefore:

```text
O(V)
```

---

## Characteristics

| Property | Description |
|---|---|
| Search Type | Heuristic Search |
| Strategy | Greedy |
| Evaluation Function | h(n) |
| Data Structure | Python List |
| Complete | Not guaranteed in general |
| Optimal | No |
| Memory Usage | O(V) |
| External Libraries | None |

---

## Difference Between BFS and Best First Search

| Feature | BFS | Best First Search |
|---|---|---|
| Selection | Based on depth/order | Based on heuristic |
| Main Structure | Queue | OPEN list |
| Uses heuristic | No | Yes |
| Evaluation | No heuristic | h(n) |
| Search behavior | Level by level | Most promising node first |
| Optimal | Yes for unit-cost edges | No |

---

## Difference Between Best First Search and A*

Best First Search uses:

```text
f(n) = h(n)
```

A* uses:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` = cost from the start node to the current node
- `h(n)` = estimated cost from the current node to the goal

A* considers both the path cost already travelled and the estimated remaining cost.

---

## Limitations

Best First Search is guided only by the heuristic value.

Therefore:

- It does not consider the actual cost already travelled.
- It does not guarantee the shortest path.
- Its result depends heavily on the quality of the heuristic.
- It may explore an unsuitable path because a node appears promising according to `h(n)`.

---

## Learning Outcomes

After completing this experiment, the following concepts were understood:

1. Working principle of Best First Search.
2. Use of heuristic functions in search.
3. Difference between uninformed and heuristic search.
4. Use of OPEN and VISITED lists.
5. Selection of the node with minimum heuristic value.
6. Difference between Best First Search and BFS.
7. Difference between Best First Search and A*.
8. Time and space complexity of a list-based implementation.
