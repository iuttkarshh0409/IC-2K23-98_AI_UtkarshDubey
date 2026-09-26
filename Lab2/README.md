# Lab 2 — Classical & Heuristic Search Algorithms

## Course

**Artificial Intelligence Lab**

**Roll No.:** IC-2K23-98  
**Student:** Utkarsh Dubey  
**Laboratory:** Lab 2  
**Unit:** Unit 2 — Search Techniques in Artificial Intelligence  
**Status:** ✅ Completed

---

# 1. Overview

Lab 2 focuses on classical and heuristic search techniques used in Artificial Intelligence for exploring problem spaces and finding solutions.

The laboratory progresses from basic systematic search to heuristic-driven optimization and informed search.

The experiments cover:

- Generate and Test
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Hill Climbing
- Best First Search
- A* Search
- State-space exploration
- Heuristic functions
- Cost-based search
- Greedy search
- Informed search
- Search performance and complexity

The implementations were developed progressively using simple Python data structures such as lists and dictionaries. This approach keeps the underlying search logic visible rather than hiding it behind advanced library implementations.

---

# 2. Laboratory Experiments

| No. | Experiment | Primary Concepts | Status |
|---|---|---|---|
| **01** | Generate and Test | Systematic Search, Candidate Generation, Goal Testing | ✅ Completed |
| **02** | Breadth-First Search | Queue, Level-Order Exploration, Visited States | ✅ Completed |
| **03** | Depth-First Search | Stack, Depth-First Exploration, Backtracking | ✅ Completed |
| **04** | Hill Climbing | Local Search, Heuristic Optimization, Local Maximum | ✅ Completed |
| **05** | Best First Search | Heuristic Search, Greedy Search, `h(n)` | ✅ Completed |
| **06** | A* Search | Informed Search, Path Cost, Heuristic, `g(n)+h(n)` | ✅ Completed |

---

# 3. Repository Structure

```text
Lab2/
│
├── 01_generate_and_test/
│   ├── generate_and_testV1.py
│   ├── README.md
│   └── outputs/
│       ├── successful_search.png
│       └── unsuccessful_search.png
│
├── 02_bfs/
│   ├── bfsV1.py
│   ├── README.md
│   └── outputs/
│       ├── bfs_from_A.png
│       ├── bfs_from_B.png
│       └── invalid_input.png
│
├── 03_dfs/
│   ├── dfsV1.py
│   ├── README.md
│   └── outputs/
│       ├── dfs_from_A.png
│       ├── dfs_from_B.png
│       └── invalid_input.png
│
├── 04_hill_climbing/
│   ├── hill_climbingV1.py
│   ├── README.md
│   └── outputs/
│       ├── hill_climbing_start_1.png
│       ├── hill_climbing_start_3.png
│       ├── hill_climbing_start_5.png
│       └── hill_climbing_start_8.png
│
├── 05_best_first_search/
│   ├── best_first_searchV1.py
│   ├── README.md
│   └── outputs/
│       ├── best_first_search_A_to_F.png
│       ├── best_first_search_A_to_E.png
│       └── invalid_input.png
│
├── 06_a_star/
│   ├── a_starV1.py
│   ├── README.md
│   └── outputs/
│       ├── a_star_A_to_F.png
│       ├── a_star_B_to_F.png
│       └── invalid_input.png
│
└── README.md
```

Each experiment contains its own implementation, documentation, and representative output screenshots.

---

# 4. Experiment 01 — Generate and Test

## Objective

To implement the Generate and Test strategy and demonstrate systematic generation of candidate solutions followed by goal testing.

## Core Concept

```text
Generate Candidate
       ↓
Test Candidate
       ↓
Goal Satisfied?
    /       \
  Yes        No
   ↓          ↓
Success    Generate Next
```

The implementation generates values within a user-defined range and tests each value against the target.

## Test Cases

Successful search:

```text
Start = 1
End = 100
Target = 64
```

Result:

```text
64 is found
Search successful
```

Unsuccessful search:

```text
Start = 1
End = 10
Target = 64
```

Result:

```text
64 is not found
Search failed
```

### Learning Focus

- Generate and Test
- Candidate generation
- Goal testing
- Systematic search
- Successful and unsuccessful search conditions

---

# 5. Experiment 02 — Breadth-First Search

## Objective

To implement Breadth-First Search for systematic graph traversal.

## Core Concept

BFS explores nodes level by level.

```text
Starting Node
      ↓
Immediate Neighbours
      ↓
Next-Level Neighbours
      ↓
Continue Until Search Completes
```

The implementation uses a Python list as a queue.

For the graph used in the experiment, starting from `A` produces:

```text
A → B → C → D → E → F
```

## Core Components

```text
Graph
Queue
Visited List
```

The process is:

```text
Add Start
    ↓
Remove Front Node
    ↓
Visit Node
    ↓
Add Unvisited Neighbours
    ↓
Repeat
```

## Test Cases

| Starting Node | Result |
|---|---|
| `A` | `A → B → C → D → E → F` |
| `B` | `B → D → E` |
| `D` | `D` |
| `X` | Invalid input |

### Learning Focus

- Breadth-First Search
- Queue-based exploration
- Level-order traversal
- Visited-state tracking
- Graph traversal
- Invalid input handling

---

# 6. Experiment 03 — Depth-First Search

## Objective

To implement Depth-First Search for graph traversal using an explicit stack.

## Core Concept

DFS explores one branch as deeply as possible before backtracking.

```text
Starting Node
      ↓
Choose Neighbour
      ↓
Explore Deeper
      ↓
No More Unvisited Nodes
      ↓
Backtrack
```

The implementation uses a Python list as a stack.

For the graph used in the experiment, starting from `A` produces:

```text
A → B → D → E → C → F
```

## Core Components

```text
Graph
Stack
Visited List
```

## Test Cases

| Starting Node | Result |
|---|---|
| `A` | `A → B → D → E → C → F` |
| `B` | `B → D → E` |
| `D` | `D` |
| `X` | Invalid input |

### Learning Focus

- Depth-First Search
- Stack-based exploration
- Depth-first traversal
- Backtracking
- Visited-state tracking
- Graph traversal

---

# 7. Experiment 04 — Hill Climbing

## Objective

To implement the Hill Climbing algorithm for local optimization.

## Function Used

```text
f(x) = -(x - 5)² + 25
```

The maximum occurs at:

```text
x = 5
f(5) = 25
```

## Core Concept

Hill Climbing repeatedly moves toward a neighboring state with a better value.

```text
Current State
      ↓
Evaluate Neighbours
      ↓
Better Neighbour?
   /        \
 Yes         No
  ↓           ↓
Move        Stop
  ↓
Repeat
```

## Search Examples

Starting from `1`:

```text
1 → 2 → 3 → 4 → 5
```

Starting from `3`:

```text
3 → 4 → 5
```

Starting from `5`:

```text
5
```

Starting from `8`:

```text
8 → 7 → 6 → 5
```

All tested starting states reach:

```text
Best State = 5
Best Value = 25
```

## Characteristics

```text
Search Type: Local Search
Strategy: Greedy Improvement
Memory: O(1)
```

## Limitations

Hill Climbing can become trapped at:

- Local maxima
- Plateaus
- Ridges

Therefore, reaching a state with no better neighboring state does not necessarily guarantee a global optimum.

### Learning Focus

- Local search
- Heuristic optimization
- Neighbor evaluation
- Greedy improvement
- Local maximum
- Search limitations

---

# 8. Experiment 05 — Best First Search

## Objective

To implement Best First Search using heuristic values to select the most promising node.

## Core Concept

Best First Search selects the node with the smallest heuristic value:

```text
f(n) = h(n)
```

Heuristic values used:

```text
A = 6
B = 4
C = 2
D = 7
E = 3
F = 0
```

For a search from `A` to `F`:

```text
A → C → F
```

The algorithm selects the node with the minimum `h(n)` from the OPEN list.

## Core Components

```text
OPEN List
VISITED List
Graph
Heuristic Function
```

### Learning Focus

- Heuristic search
- Greedy search
- Heuristic functions
- OPEN and VISITED lists
- Minimum heuristic selection
- Difference between BFS and heuristic search

---

# 9. Experiment 06 — A* Search

## Objective

To implement A* Search using actual path cost and heuristic estimation to find a cost-effective path to a goal.

## Core Concept

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

## Weighted Graph

The experiment uses these edge costs:

```text
A → B = 1
A → C = 4
B → D = 5
B → E = 2
C → F = 3
E → F = 1
```

Heuristic values:

```text
A = 5
B = 3
C = 3
D = 6
E = 1
F = 0
```

## Search Process

Starting from `A` and searching for `F`:

```text
A → B → E → F
```

Total path cost:

```text
1 + 2 + 1 = 4
```

## Core Components

```text
OPEN List
VISITED List
g_score
Heuristic
Edge Costs
f(n)
```

The algorithm selects the node with the smallest:

```text
f(n) = g(n) + h(n)
```

and updates path costs when a cheaper route is discovered.

### Learning Focus

- Informed search
- Path cost
- Heuristic estimation
- `g(n)`, `h(n)`, and `f(n)`
- Cost-aware search
- Comparison with Best First Search

---

# 10. Comparison of Search Algorithms

| Algorithm | Search Type | Main Mechanism | Evaluation |
|---|---|---|---|
| Generate & Test | Systematic | Generate and test candidates | Goal test |
| BFS | Uninformed | Level-order exploration | Depth/order |
| DFS | Uninformed | Deep exploration | Depth/order |
| Hill Climbing | Local | Move to better neighbour | State value |
| Best First | Informed | Greedy heuristic search | `h(n)` |
| A* | Informed | Cost + heuristic | `g(n) + h(n)` |

---

# 11. BFS vs DFS

BFS and DFS are both uninformed search techniques, but they explore the search space differently.

```text
BFS
 ↓
Level by Level
 ↓
Queue
```

while:

```text
DFS
 ↓
Depth First
 ↓
Stack
```

For unit-cost graphs, BFS can find a shortest path in terms of number of edges, while DFS does not generally guarantee a shortest path.

---

# 12. Best First Search vs A*

The major distinction between the two informed search algorithms is the evaluation function.

### Best First Search

```text
f(n) = h(n)
```

It considers only the estimated remaining cost.

### A*

```text
f(n) = g(n) + h(n)
```

It considers both:

```text
Actual cost travelled
+
Estimated cost remaining
```

This makes A* cost-aware rather than purely greedy.

---

# 13. Performance Analysis

The laboratory implementations use simple Python lists and dictionaries to make the search mechanisms transparent.

### Generate & Test

For a range of `n` candidates:

```text
Worst Case: O(n)
Space: O(1)
```

### BFS

For a graph with `V` vertices and `E` edges, standard BFS has:

```text
Time: O(V + E)
Space: O(V)
```

The current implementation uses `pop(0)` on a Python list rather than `collections.deque`, which introduces additional overhead for large queues.

### DFS

For a graph with `V` vertices and `E` edges:

```text
Time: O(V + E)
Space: O(V)
```

### Hill Climbing

For `n` iterations:

```text
Time: O(n)
Space: O(1)
```

### Best First Search

The V1 implementation linearly scans the OPEN list to find the minimum heuristic.

```text
Worst Case: O(V²)
Space: O(V)
```

### A*

The V1 implementation linearly scans the OPEN list to find the minimum `f(n)`.

```text
Worst Case: O(V²)
Space: O(V)
```

More efficient implementations can use priority queues to improve next-node selection.

---

# 14. Output Artifacts

Each experiment contains representative execution screenshots.

```text
01_generate_and_test/
└── outputs/
    ├── successful_search.png
    └── unsuccessful_search.png

02_bfs/
└── outputs/
    ├── bfs_from_A.png
    ├── bfs_from_B.png
    └── invalid_input.png

03_dfs/
└── outputs/
    ├── dfs_from_A.png
    ├── dfs_from_B.png
    └── invalid_input.png

04_hill_climbing/
└── outputs/
    ├── hill_climbing_start_1.png
    ├── hill_climbing_start_3.png
    ├── hill_climbing_start_5.png
    └── hill_climbing_start_8.png

05_best_first_search/
└── outputs/
    ├── best_first_search_A_to_F.png
    ├── best_first_search_A_to_E.png
    └── invalid_input.png

06_a_star/
└── outputs/
    ├── a_star_A_to_F.png
    ├── a_star_B_to_F.png
    └── invalid_input.png
```

---

# 15. Overall Learning Progression

```text
Generate & Test
      ↓
Basic Systematic Search
      ↓
BFS
      ↓
Level-Based Graph Search
      ↓
DFS
      ↓
Depth-Based Graph Search
      ↓
Hill Climbing
      ↓
Local Heuristic Optimization
      ↓
Best First Search
      ↓
Greedy Heuristic Search
      ↓
A* Search
      ↓
Cost + Heuristic Informed Search
```

This progression moves from simple candidate generation to increasingly sophisticated search strategies.

---

# 16. Concepts Covered Across Lab 2

### Uninformed Search

```text
BFS
DFS
```

### Systematic Search

```text
Generate & Test
```

### Local Search

```text
Hill Climbing
```

### Heuristic Search

```text
Best First Search
```

### Informed Search

```text
A*
```

### Core Search Concepts

```text
Search Space
States
Nodes
Edges
Goal Testing
Visited States
OPEN List
Heuristic Function
Path Cost
Evaluation Function
State Exploration
Solution Path
Search Complexity
```

---

# 17. Learning Outcomes

After completing Lab 2, the following concepts were implemented and understood:

- Generate and Test search
- Breadth-First Search
- Depth-First Search
- Queue-based exploration
- Stack-based exploration
- Visited-state tracking
- Local search
- Hill Climbing
- Heuristic functions
- Greedy search
- Best First Search
- Path cost
- Informed search
- A* Search
- `g(n)`, `h(n)`, and `f(n)`
- OPEN and VISITED lists
- Goal testing
- Search-space exploration
- Time and space complexity
- Comparison of search strategies

---

# 18. Conclusion

Lab 2 established the fundamental search techniques used in Artificial Intelligence for exploring problem spaces and finding solutions.

The experiments progressed from simple candidate generation and systematic graph traversal to heuristic and informed search:

```text
Generate & Test
      ↓
BFS / DFS
      ↓
Hill Climbing
      ↓
Best First Search
      ↓
A* Search
```

The laboratory demonstrates how different search strategies make different decisions about which state to explore next.

The progression from:

```text
No heuristic
      ↓
Local heuristic
      ↓
Greedy heuristic
      ↓
Path cost + heuristic
```

provides a practical foundation for understanding intelligent search and optimization techniques in Artificial Intelligence.

---

## Lab Status

**Lab 2: ✅ COMPLETED**

**Next:** Lab 3 — Data Preprocessing, EDA & Visualization
