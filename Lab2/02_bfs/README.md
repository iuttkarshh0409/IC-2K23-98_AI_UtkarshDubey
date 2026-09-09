# Experiment 02: Breadth First Search (BFS)

## Aim

To implement the Breadth First Search (BFS) algorithm for traversing a graph and understand its level-by-level search strategy using a Python list as a queue.

## Problem Statement

Implement Breadth First Search to traverse a graph starting from a user-specified node. The algorithm should visit nodes level by level, maintain a list of visited nodes, and display the final traversal order.

## Concept

Breadth First Search is an uninformed search algorithm that explores all nodes at the current depth before moving to nodes at the next depth.

BFS follows the **First In, First Out (FIFO)** principle.

In this implementation, a Python list is used to perform queue operations:

- `append()` adds a node to the end of the queue.
- `pop(0)` removes the first node from the queue.

## Graph Used

The following graph is used for the experiment:

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
2. Take the starting node as input from the user.
3. Check whether the starting node exists in the graph.
4. Initialize a queue with the starting node.
5. Initialize an empty visited list.
6. While the queue is not empty:
   - Remove the first node from the queue.
   - Check whether it has already been visited.
   - If not visited, add it to the visited list.
   - Display the current node.
   - Add its unvisited neighbours to the end of the queue.
7. Continue until the queue becomes empty.
8. Display the BFS traversal order.

## Pseudocode

```text
START

Define graph

Input starting node

IF starting node is not present:
    Display "Invalid starting node"
    STOP

Create queue containing starting node
Create empty visited list

WHILE queue is not empty:

    Remove first node from queue

    IF node is not in visited:

        Add node to visited
        Display node

        FOR each neighbour of node:

            IF neighbour is not in visited:
                Add neighbour to queue

Display BFS traversal

END
```

## Implementation

The implementation is provided in:

```text
bfsV1.py
```

The program uses only Python's built-in list data structure for the BFS queue. No external libraries or `deque` are used.

## Sample Test Case 1: BFS Starting from A

### Input

```text
Enter starting node: A
```

### Output

```text
Visiting: A
Visiting: B
Visiting: C
Visiting: D
Visiting: E
Visiting: F

BFS Traversal: A -> B -> C -> D -> E -> F
```

### Result

The graph is traversed level by level starting from node `A`.

## Sample Test Case 2: BFS Starting from B

### Input

```text
Enter starting node: B
```

### Output

```text
Visiting: B
Visiting: D
Visiting: E

BFS Traversal: B -> D -> E
```

### Result

The traversal correctly starts from node `B` and visits its reachable nodes.

## Sample Test Case 3: Leaf Node

### Input

```text
Enter starting node: D
```

### Output

```text
Visiting: D

BFS Traversal: D
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

For a graph represented using an adjacency list, the standard BFS traversal has:

- **Time Complexity:** `O(V + E)`
- **Space Complexity:** `O(V)`

The queue and visited list can contain up to `V` nodes.

For this implementation, `queue.pop(0)` is used because the experiment is intentionally implemented using a basic Python list. Removing the first element from a Python list can require shifting the remaining elements, so this implementation is less efficient than using `collections.deque` for very large graphs.

However, the list-based approach makes the FIFO behaviour of BFS easier to understand and demonstrates the underlying algorithm clearly.

## Output / Screenshots

The output screenshots are stored in the `outputs/` directory.

Recommended organization:

```text
outputs/
├── bfs_from_A.png
├── bfs_from_B.png
└── invalid_input.png
```

The screenshots demonstrate:

1. BFS traversal starting from node `A`.
2. BFS traversal starting from node `B`.
3. Handling of an invalid starting node.

## Learning Outcomes

After completing this experiment, the following concepts were understood:

- Working with graphs using adjacency lists.
- Understanding the Breadth First Search algorithm.
- Understanding level-by-level graph traversal.
- Understanding the FIFO principle.
- Implementing a queue using a Python list.
- Maintaining a visited list to avoid repeated traversal.
- Handling valid and invalid user inputs.
- Understanding the time and space complexity of BFS.

## Conclusion

Breadth First Search was successfully implemented using a Python list as a queue. The program correctly traverses the graph level by level, maintains visited nodes, handles different starting nodes, and detects invalid input.
