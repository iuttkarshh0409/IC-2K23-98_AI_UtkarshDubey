# Water Jug Problem

## 1. Aim

To formulate and implement the Water Jug Problem using state-space representation and demonstrate state transitions, valid operations, visited-state handling, and automated state-space search.

---

## 2. Problem Statement

Given two water jugs of user-defined capacities and an initially empty state, measure a specified target amount of water using the available jug operations.

The allowed operations are:

1. Fill Jug 1 completely.
2. Fill Jug 2 completely.
3. Empty Jug 1 completely.
4. Empty Jug 2 completely.
5. Pour water from Jug 1 into Jug 2 until Jug 1 is empty or Jug 2 is full.
6. Pour water from Jug 2 into Jug 1 until Jug 2 is empty or Jug 1 is full.

The program should represent the problem as a state space and determine a sequence of valid operations that reaches the target amount.

---

## 3. State Space Representation

A state is represented as:

```text
(x, y)
```

where:

* `x` = current amount of water in Jug 1
* `y` = current amount of water in Jug 2

For jug capacities `C1` and `C2`:

```text
0 ≤ x ≤ C1
0 ≤ y ≤ C2
```

The initial state is:

```text
(0, 0)
```

The goal state is any state satisfying:

```text
x = target
OR
y = target
```

For example, for 4L and 3L jugs with a target of 2L, valid goal states include:

```text
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(0, 2)
(1, 2)
(2, 2)
(3, 2)
(4, 2)
```

The actual goal condition used by the program is whether either jug contains the target amount.

---

## 4. Operators

The six operators used to generate new states are:

| Operator           | Description                                          |
| ------------------ | ---------------------------------------------------- |
| Fill Jug 1         | Fill Jug 1 to its capacity                           |
| Fill Jug 2         | Fill Jug 2 to its capacity                           |
| Empty Jug 1        | Remove all water from Jug 1                          |
| Empty Jug 2        | Remove all water from Jug 2                          |
| Pour Jug 1 → Jug 2 | Transfer water until Jug 1 is empty or Jug 2 is full |
| Pour Jug 2 → Jug 1 | Transfer water until Jug 2 is empty or Jug 1 is full |

For a pouring operation, the amount transferred is determined by:

```text
minimum(
    water available in source jug,
    free capacity in destination jug
)
```

---

## 5. Algorithm

### Interactive State-Space Exploration

1. Accept the capacities of both jugs and the target amount from the user.
2. Initialize the state as `(0, 0)`.
3. Generate the six possible operations.
4. Apply an operation to generate a resultant state.
5. Reject the operation if it produces no change in state.
6. Track states that have already been visited.
7. Reject a transition if its resultant state has already been visited.
8. Record every meaningful state transition.
9. Check whether the target amount has been reached.
10. Continue until the target is reached or no unexplored state remains.

### Automated Search

The automated version maintains a collection of pending states.

For each state:

1. Remove a state from the pending collection.
2. Check whether it satisfies the goal condition.
3. Generate its possible next states.
4. Ignore invalid, unchanged, or already visited states.
5. Add newly discovered states to the pending collection.
6. Continue until the target state is found or the search space is exhausted.

---

## 6. Implementation Versions

The implementation was developed incrementally to understand the problem before introducing automated search.

| Version          | Development Stage                                         |
| ---------------- | --------------------------------------------------------- |
| `water_jugV1.py` | Interactive execution of the six jug operations           |
| `water_jugV2.py` | State transition history and complete path tracking       |
| `water_jugV3.py` | Modular implementation using reusable operation functions |
| `water_jugV4.py` | Visited-state tracking and repeated-state rejection       |
| `water_jugV5.py` | Generation and display of possible next transitions       |
| `water_jugV6.py` | Automated state-space exploration                         |

This progression demonstrates the development from basic problem interaction to state-space based problem solving.

---

##  State Space Representation

The Water Jug Problem can be represented as a state-space graph.

A state is represented as `(x, y)`, where:

- `x` = amount of water in the 3L jug
- `y` = amount of water in the 5L jug
- Initial state = `(0, 0)`
- Goal condition = either jug contains exactly 4L

### Complete State Space

```mermaid
flowchart TB
    T["WATER JUG STATE SPACE<br/>Jug 1 = 3L · Jug 2 = 5L · Target = 4L"]

    subgraph STATES["All 24 Possible States (x, y)"]
        direction TB

        subgraph Y5["5L Jug = 5"]
            direction LR
            S05["(0,5)"] --- S15["(1,5)"] --- S25["(2,5)"] --- S35["(3,5)"]
        end

        subgraph Y4["5L Jug = 4 · GOAL STATES"]
            direction LR
            S04["(0,4)"] --- S14["(1,4)"] --- S24["(2,4)"] --- S34["(3,4) ✓"]
        end

        subgraph Y3["5L Jug = 3"]
            direction LR
            S03["(0,3)"] --- S13["(1,3)"] --- S23["(2,3)"] --- S33["(3,3)"]
        end

        subgraph Y2["5L Jug = 2"]
            direction LR
            S02["(0,2)"] --- S12["(1,2)"] --- S22["(2,2)"] --- S32["(3,2)"]
        end

        subgraph Y1["5L Jug = 1"]
            direction LR
            S01["(0,1)"] --- S11["(1,1)"] --- S21["(2,1)"] --- S31["(3,1)"]
        end

        subgraph Y0["5L Jug = 0"]
            direction LR
            S00["(0,0) START"] --- S10["(1,0)"] --- S20["(2,0)"] --- S30["(3,0)"]
        end
    end

    T --> STATES

    subgraph PATH["One Valid Solution Path"]
        direction LR
        P0["(0,0)"] -->|Fill 5L| P1["(0,5)"]
        P1 -->|Pour 5L → 3L| P2["(3,2)"]
        P2 -->|Empty 3L| P3["(0,2)"]
        P3 -->|Pour 5L → 3L| P4["(2,0)"]
        P4 -->|Fill 5L| P5["(2,5)"]
        P5 -->|Pour 5L → 3L| P6["(3,4) GOAL"]
    end

    STATES --> PATH

    classDef start fill:#4b3b72,color:#fff,stroke:#4b3b72,stroke-width:3px;
    classDef goal fill:#f5a623,color:#111,stroke:#8a5a00,stroke-width:3px;
    classDef normal fill:#f3eefb,color:#332b45,stroke:#b8a9d6;

    class S00,P0 start;
    class S04,S14,S24,S34,P6 goal;
    class S05,S15,S25,S35,S03,S13,S23,S33,S02,S12,S22,S32,S01,S11,S21,S31,S10,S20,S30,P1,P2,P3,P4,P5 normal;

---

## 7. State Transition Example

For 4L and 3L jugs, starting from:

```text
(0, 0)
```

one possible sequence is:

```text
(0, 0)
    |
    | Fill Jug 2
    ↓
(0, 3)
    |
    | Pour Jug 2 → Jug 1
    ↓
(3, 0)
    |
    | Fill Jug 2
    ↓
(3, 3)
    |
    | Pour Jug 2 → Jug 1
    ↓
(4, 2)
```

The target amount of 2L is reached in Jug 2.

---

## 8. Result

The Water Jug Problem was successfully formulated as a state-space problem.

The implementation can:

* Represent the current state of both jugs.
* Apply all six valid operations.
* Generate resultant states.
* Reject non-meaningful transitions.
* Track visited states.
* Record state transitions and solution paths.
* Generate possible next states.
* Automatically explore the state space to find a solution.

For the standard configuration:

```text
Jug 1 Capacity = 4L
Jug 2 Capacity = 3L
Target = 2L
```

a valid solution is obtained with the target amount present in one of the jugs.

---

## 9. Performance Analysis

For the Water Jug Problem, the state space is finite.

For jug capacities `C1` and `C2`, the maximum number of possible states is:

```text
(C1 + 1) × (C2 + 1)
```

For 4L and 3L jugs:

```text
(4 + 1) × (3 + 1)
= 5 × 4
= 20 possible states
```

Visited-state tracking prevents the search from repeatedly exploring the same state.

Relevant measures for the experiment include:

* Number of states visited
* Number of operations in the solution
* Number of generated transitions
* Execution time for automated search

For this small problem, execution time is very low. Therefore, the number of explored states and solution depth provide more meaningful measures than raw execution time.

---

## 10. Observations

1. The Water Jug Problem can be naturally represented using a tuple-based state representation.
2. Each legal operation produces a transition from one state to another.
3. Different operations can produce the same state.
4. Some operations do not change the state and can therefore be discarded.
5. Maintaining a visited-state set prevents repeated exploration.
6. The problem can be represented as a graph where states are nodes and operations are edges.
7. Automated search can find a solution without requiring the user to manually select every operation.
8. The same state-space representation can later be used with search strategies such as BFS and DFS.

---

## 11. Learning Outcomes

After completing this experiment, the following concepts were understood and implemented:

* AI problem formulation
* State-space representation
* Initial state and goal state
* State transitions
* Operators in a production/search problem
* Valid and non-meaningful transitions
* Visited-state tracking
* State-space exploration
* Solution path representation
* Basic automated search

---

## 12. Files

```text
water_jugV1.py
water_jugV2.py
water_jugV3.py
water_jugV4.py
water_jugV5.py
water_jugV6.py
```

Each version represents an incremental improvement in the implementation.

---

## 13. Conclusion

The Water Jug Problem was successfully implemented as a state-space problem. Starting from an interactive implementation, the experiment was progressively enhanced with state transition tracking, modular operations, visited-state handling, transition generation, and automated state-space exploration.

The experiment establishes the foundation required for studying classical AI search algorithms, where the same state space can be explored using different search strategies.
