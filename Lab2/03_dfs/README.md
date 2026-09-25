# Experiment 03: Depth First Search (DFS)

## Aim

To implement the Depth First Search (DFS) algorithm for traversing a graph and understand its depth-first search strategy using a Python list as a stack.

## Problem Statement

Implement Depth First Search to traverse a graph starting from a user-specified node. The algorithm should explore a path as deeply as possible before backtracking and maintain a list of visited nodes to avoid repeated traversal.

## Concept

Depth First Search is an uninformed search algorithm that explores one branch of a graph as deeply as possible before backtracking to explore other branches.

DFS follows the **Last In, First Out (LIFO)** principle.

In this implementation, a Python list is used as a stack:

- `append()` adds a node to the top of the stack.
- `pop()` removes the last node from the stack.

## Graph Used

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

Graph representation:

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
```

## Algorithm

1. Define the graph using an adjacency list.
2. Take the starting node as input.
3. Check whether the starting node exists in the graph.
4. Initialize a stack with the starting node.
5. Initialize an empty visited list.
6. While the stack is not empty:
   - Remove the last node from the stack.
   - Check whether it has already been visited.
   - If not visited, add it to the visited list.
   - Display the current node.
   - Add its unvisited neighbours to the stack.
7. Continue until the stack becomes empty.
8. Display the DFS traversal order.

## Pseudocode

```text
START

Define graph

Input starting node

IF starting node is not present:
    Display "Invalid starting node"
    STOP

Create stack containing starting node
Create empty visited list

WHILE stack is not empty:

    Remove last node from stack

    IF node is not in visited:

        Add node to visited
        Display node

        FOR each neighbour of node in reverse order:

            IF neighbour is not in visited:
                Add neighbour to stack

Display DFS traversal

END
```

## Implementation

The implementation is provided in:

```text
dfsV1.py
```

The program uses only Python's built-in list data structure as a stack. No external libraries are used.

The `pop()` operation removes the last element of the list, providing the required LIFO behaviour.

The neighbours are processed in reverse order so that the traversal follows the intuitive left-to-right order of the graph.

## Sample Test Case 1: DFS Starting from A

### Input

```text
Enter starting node: A
```

### Output

```text
Visiting: A
Visiting: B
Visiting: D
Visiting: E
Visiting: C
Visiting: F

DFS Traversal: A -> B -> D -> E -> C -> F
```

### Result

The graph is traversed depth-first starting from node `A`.

## Sample Test Case 2: DFS Starting from B

### Input

```text
Enter starting node: B
```

### Output

```text
Visiting: B
Visiting: D
Visiting: E

DFS Traversal: B -> D -> E
```

### Result

The traversal correctly starts from node `B` and explores its branch before terminating.

## Sample Test Case 3: Leaf Node

### Input

```text
Enter starting node: D
```

### Output

```text
Visiting: D

DFS Traversal: D
```

### Result

Since `D` has no neighbours, only the starting node is visited.

## Sample Test Case 4: Invalid Input

### Input

```text
Enter starting node: X
```

### Output

```text
Invalid starting node.
```

### Result

The program correctly identifies that `X` does not exist in the graph and terminates without performing the search.

## Performance Analysis

Let:

- `V` = number of vertices
- `E` = number of edges

For a graph represented using an adjacency list:

- **Time Complexity:** `O(V + E)`
- **Space Complexity:** `O(V)`

The stack and visited list can contain up to `V` nodes.

The iterative list-based implementation clearly demonstrates the LIFO behaviour of DFS. Python list operations `append()` and `pop()` from the end are efficient for stack operations.

## Output / Screenshots

The output screenshots are stored in the `outputs/` directory.

```text
outputs/
├── dfs_from_A.png
├── dfs_from_B.png
└── invalid_input.png
```

The screenshots demonstrate:

1. DFS traversal starting from node `A`.
2. DFS traversal starting from node `B`.
3. Handling of an invalid starting node.

## Learning Outcomes

After completing this experiment, the following concepts were understood:

- Working with graphs using adjacency lists.
- Understanding the Depth First Search algorithm.
- Understanding depth-first graph traversal.
- Understanding the LIFO principle.
- Implementing a stack using a Python list.
- Maintaining a visited list to avoid repeated traversal.
- Understanding the role of neighbour ordering in iterative DFS.
- Handling valid and invalid user inputs.
- Understanding the time and space complexity of DFS.

## BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Basic structure | Queue | Stack |
| Principle | FIFO | LIFO |
| Traversal | Level by level | Depth first |
| Python list operation | `pop(0)` | `pop()` |
| Example from A | A -> B -> C -> D -> E -> F | A -> B -> D -> E -> C -> F |

## Conclusion

Depth First Search was successfully implemented using a Python list as a stack. The program correctly explores the graph depth-first, maintains visited nodes, handles different starting nodes, and detects invalid input.
