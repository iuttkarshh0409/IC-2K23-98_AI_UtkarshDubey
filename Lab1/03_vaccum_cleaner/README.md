# Vacuum Cleaner Problem

## 1. Aim

To implement the classical Vacuum Cleaner Problem using state-space representation and demonstrate state transitions, valid actions, goal testing, and a simple state-based intelligent agent.

## 2. Problem Statement

The Vacuum Cleaner Problem consists of a vacuum cleaner operating in two rooms, Room 1 and Room 2.

Each room can be either `Clean` or `Dirty`, and the vacuum cleaner can be positioned in either room.

The objective is to clean both rooms using a sequence of valid actions.

Two implementations are developed:

- **V1:** Interactive state-transition system where the user selects the actions.
- **V2:** State-based intelligent agent that selects actions automatically based on the current state.

## 3. State Representation

A state is represented as:

```text
(Room_1_State, Room_2_State, Vacuum_Position)
```

where:

- `Room_1_State` ∈ `{Clean, Dirty}`
- `Room_2_State` ∈ `{Clean, Dirty}`
- `Vacuum_Position` ∈ `{A, B}`

Example:

```text
(Dirty, Dirty, A)
```

represents:

```text
Room 1 → Dirty
Room 2 → Dirty
Vacuum → Room 1
```

Since each room has two possible states and the vacuum has two possible positions:

```text
2 × 2 × 2 = 8
```

possible states exist in the complete state space.

## 4. Initial State

The default initial state used in the implementation is:

```text
(Dirty, Dirty, A)
```

This means both rooms are dirty and the vacuum starts in Room 1.

## 5. Goal State

The goal is reached when both rooms are clean.

Therefore:

```text
Room 1 = Clean
AND
Room 2 = Clean
```

Valid goal states are:

```text
(Clean, Clean, A)
(Clean, Clean, B)
```

## 6. Available Actions

### 1. Suck

The vacuum cleans the room in which it is currently located.

### 2. Move to Room 1

The vacuum moves to Room 1 without changing room cleanliness.

### 3. Move to Room 2

The vacuum moves to Room 2 without changing room cleanliness.

## 7. Constraints

1. The vacuum cleaner can only move between Room 1 and Room 2.
2. The vacuum cleaner can only clean the room in which it is currently located.
3. The vacuum cleaner cannot clean an already clean room. Such a transition produces no state change and is discarded.
4. The vacuum cleaner can clean only one room at a time.
5. The program terminates when both rooms are clean and displays the total number of operations and the final state.

## 8. V1 - Interactive State-Transition System

V1 allows the user to manually select an operation.

```text
Current State
      ↓
User Selects Action
      ↓
Apply Action
      ↓
Generate Resultant State
      ↓
Check for State Change
      ↓
Record Transition
      ↓
Check Goal
```

A non-meaningful transition is discarded if:

```text
Resultant State == Previous State
```

## 9. V2 - State-Based Intelligent Agent

V2 moves action selection from the user to the vacuum cleaner.

The agent follows:

```text
IF both rooms are clean
    → terminate

ELSE IF current room is dirty
    → Suck

ELSE
    → Move to the other room
```

Decision flow:

```text
             Current State
                   ↓
            Are both rooms
                clean?
              /        \
            YES         NO
             ↓           ↓
          STOP      Is current room
                       dirty?
                      /     \
                    YES      NO
                     ↓        ↓
                   SUCK    Move to
                           other room
                     \       /
                      \     /
                       ↓   ↓
                    New State
                       ↓
                  Goal Test
                       ↓
                    Repeat
```

## 10. V1 vs V2

| Aspect | V1 | V2 |
|---|---|---|
| Action selection | User | Vacuum agent |
| State representation | Same | Same |
| State transitions | Manual | Automatic |
| Goal test | Yes | Yes |
| Main concept | State-space simulation | State-based intelligent agent |

The main conceptual upgrade is:

```text
V1:
Human → chooses action → State Transition

V2:
Agent observes state → chooses action → State Transition
```

## 11. Algorithm

### V1

1. Initialize the current state.
2. Display available operations.
3. Take an operation from the user.
4. Store the previous state.
5. Apply the selected operation.
6. Compare the previous and resultant states.
7. Discard the transition if there is no state change.
8. Record the valid transition and increment the operation count.
9. Check whether both rooms are clean.
10. Repeat until the goal is reached or the user exits.

### V2

1. Initialize the current state.
2. Check whether both rooms are clean.
3. If the goal is reached, terminate.
4. Identify the current vacuum position.
5. If the current room is dirty, perform `Suck`.
6. Otherwise, move to the other room.
7. Compare the previous and resultant states.
8. Record the valid transition and increment the operation count.
9. Repeat until both rooms are clean.
10. Display the total operations and final state.

## 12. State-Space Representation

A complete state is represented by:

```text
(Room 1 State, Room 2 State, Vacuum Position)
```

There are 8 possible states. Actions create transitions between these states.

The state-space diagram is provided in:

```text
outputs/diagrams/vacuum_cleaner_state_space.png
```

## 13. Example Execution

For:

```text
(Dirty, Dirty, A)
```

V2 produces:

```text
Step 1
(Dirty, Dirty, A)
        ↓ Suck Room 1
(Clean, Dirty, A)

Step 2
(Clean, Dirty, A)
        ↓ Move to Room 2
(Clean, Dirty, B)

Step 3
(Clean, Dirty, B)
        ↓ Suck Room 2
(Clean, Clean, B)
```

The goal is reached after 3 operations.

Final state:

```text
(Clean, Clean, B)
```

## 14. Results

### V1

- User-controlled actions were implemented.
- State transitions were displayed.
- Non-meaningful transitions were detected and discarded.
- The goal state was detected.
- Total operations and final state were displayed.

### V2

- The vacuum cleaner autonomously selected actions.
- The agent responded to the current state.
- Dirty rooms were cleaned only when the vacuum was present.
- The agent moved to the other room when the current room was clean.
- Execution terminated when both rooms became clean.

## 15. Performance Analysis

This is a small deterministic state-space problem, so raw execution time is not particularly meaningful.

Relevant measures:

- Possible states: **8**
- Operations for default initial state: **3**
- Goal reached: **Yes**
- Final state: `(Clean, Clean, B)`

## 16. Observations

1. A complete state representation includes both room conditions and vacuum position.
2. Actions transform one state into another.
3. Non-meaningful transitions should be rejected.
4. Goal testing determines when the problem is solved.
5. V1 demonstrates state-space interaction through user-selected actions.
6. V2 demonstrates a simple state-based intelligent agent.
7. The agent selects actions based on the current state.
8. The same state representation supports interactive and autonomous behavior.

## 17. Learning Outcomes

- State-space representation
- State transitions
- Initial and goal states
- Operators/actions
- Goal testing
- Constraint handling
- Non-meaningful transition detection
- Interactive problem solving
- State-based intelligent agents
- Autonomous action selection
- Agent-environment interaction

## 18. Output Artifacts

```text
outputs/
├── screenshots/
│   ├── v1_interactive_execution.png
│   └── v2_intelligent_agent.png
│
└── diagrams/
    └── vacuum_cleaner_state_space.png
```

## 19. Conclusion

The Vacuum Cleaner Problem was successfully formulated as a state-space problem and implemented in two stages.

V1 demonstrated manual state transitions through user-selected actions, while V2 extended the system into a simple intelligent agent capable of observing its current state and selecting an appropriate action automatically.

The experiment demonstrates how state representation, actions, constraints, and goal testing form the foundation of intelligent problem solving in Artificial Intelligence.
