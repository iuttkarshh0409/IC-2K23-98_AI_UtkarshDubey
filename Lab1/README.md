# Lab 1 — AI Problem Formulation & Intelligent Problem Solving

## Course

**Artificial Intelligence Lab**

**Roll No.:** IC-2K23-98  
**Student:** Utkarsh Dubey  
**Laboratory:** Lab 1  
**Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving  
**Status:** ✅ Completed

---

## 1. Overview

Lab 1 introduces the foundations of Artificial Intelligence through classical problem-solving and symbolic reasoning techniques.

The laboratory focuses on how an AI problem can be represented using:

- States
- State spaces
- Initial and goal states
- Operators / actions
- Production rules
- Constraints
- Knowledge
- Inference
- Goal testing
- State-space search

The experiments were developed progressively, beginning with manually controlled state transitions and rule-based reasoning and moving toward automatic state-space exploration using BFS.

---

# 2. Laboratory Experiments

| No. | Experiment | Primary Concepts | Status |
|---|---|---|---|
| **01** | Production System | Facts, Production Rules, Forward Chaining, Backward Chaining | ✅ Completed |
| **02** | Water Jug Problem | State Space, Operators, Constraints, Goal Testing | ✅ Completed |
| **03** | Vacuum Cleaner Problem | State Representation, State Transitions, Intelligent Agent | ✅ Completed |
| **04** | Rule-Based Decision Making | Knowledge Representation, Rule Evaluation, Decision Support | ✅ Completed |
| **05** | Missionaries & Cannibals | State Space, Constraints, BFS, Search | ✅ Completed |

---

# 3. Repository Structure

```text
Lab1/
│
├── 01_production_system/
│   ├── production_systemV1.py
│   ├── production_systemV2.py
│   ├── README.md
│   └── outputs/
│       ├── screenshots/
│       └── diagrams/
│
├── 02_water_jug/
│   ├── water_jugV1.py
│   ├── water_jugV2.py
│   ├── water_jugV3.py
│   ├── water_jugV4.py
│   ├── water_jugV5.py
│   ├── water_jugV6.py
│   ├── README.md
│   └── outputs/
│       ├── screenshots/
│       └── diagrams/
│
├── 03_vacuum_cleaner/
│   ├── vacuum_cleanerV1.py
│   ├── vacuum_cleanerV2.py
│   ├── README.md
│   └── outputs/
│       ├── screenshots/
│       └── diagrams/
│
├── 04_rule_based_decision/
│   ├── rule_based_decisionV1.py
│   ├── rule_based_decisionV2.py
│   ├── README.md
│   └── outputs/
│       ├── screenshots/
│       └── diagrams/
│
├── 05_missionaries_and_cannibals/
│   ├── missionaries_and_cannibalsV1.py
│   ├── missionaries_and_cannibalsV2.py
│   ├── README.md
│   └── outputs/
│       ├── screenshots/
│       └── diagrams/
│
└── README.md
```

Each experiment has its own detailed README and output artifacts.

---

# 4. Experiment 01 — Production System

## Objective

To implement a production-rule system and demonstrate forward chaining and rule-based inference.

## Core Representation

The system consists of:

```text
Initial Facts
      ↓
Production Rules
      ↓
Rule Matching
      ↓
Rule Firing
      ↓
Derived Facts
```

## V1

V1 demonstrates forward chaining for academic decision making.

Example:

```text
is_enrolled
+
paid_fees
      ↓
confirm_enrollment
```

Then:

```text
confirm_enrollment
+
attendance_high
+
marks_good
      ↓
academically_eligible
```

And finally:

```text
academically_eligible
+
assignments_complete
      ↓
eligible_for_exam
```

## V2

V2 extends the production-system experiment to include the complementary reasoning approach required for the laboratory work:

- Forward chaining
- Backward chaining

The experiment demonstrates how the same knowledge base can be used for both data-driven and goal-driven reasoning.

### Learning Focus

- Production systems
- Working memory
- Production rules
- Forward chaining
- Backward chaining
- Inference traces

---

# 5. Experiment 02 — Water Jug Problem

## Objective

To formulate the Water Jug Problem as a state-space problem and implement valid state transitions.

## State Representation

```text
(Jug 1 Amount, Jug 2 Amount)
```

For example:

```text
(0, 0)
```

represents two empty jugs.

## Operators

The system supports:

```text
Fill Jug 1
Fill Jug 2
Empty Jug 1
Empty Jug 2
Pour Jug 1 → Jug 2
Pour Jug 2 → Jug 1
```

## Constraints

Transitions that do not change the state are discarded.

The program also checks whether the target amount has been reached after a valid transition.

## Development

The experiment was progressively developed through multiple versions:

```text
V1 → Basic interactive transitions
V2 → Transition validation
V3 → Improved state handling
V4 → Additional constraints
V5 → Efficiency improvements
V6 → Final experimental version
```

The final implementation successfully measures the target amount while displaying the state-transition process.

### Learning Focus

- State representation
- Operators
- State transitions
- Constraints
- Goal testing
- Interactive problem solving

---

# 6. Experiment 03 — Vacuum Cleaner Problem

## Objective

To model a simple intelligent agent operating in an environment consisting of two rooms.

## State Representation

```text
(Room 1 State, Room 2 State, Vacuum Position)
```

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

## Actions

The vacuum can:

```text
Clean current room
Move to Room 1
Move to Room 2
```

## Constraints

1. The vacuum can only move between the two rooms.
2. The vacuum can only clean the room it currently occupies.
3. Cleaning an already clean room produces no state change and is discarded.
4. Only one room can be cleaned by a single cleaning action.
5. Execution terminates when both rooms are clean.

## Versions

### V1

Interactive state-transition system.

### V2

State-based intelligent agent that automatically chooses its next action based on the current state.

### Learning Focus

- State representation
- Environment and agent
- State transitions
- Goal testing
- Intelligent agent behavior
- Autonomous action selection

---

# 7. Experiment 04 — Rule-Based Decision Making

## Objective

To develop an academic decision-support system using rule-based reasoning.

The system accepts student information, converts it into facts, evaluates rules, derives additional knowledge, and generates a decision.

## Decision Pipeline

```text
Student Information
        ↓
Fact Generation
        ↓
Rule Evaluation
        ↓
Derived Knowledge
        ↓
Decision + Reasons
```

## Production Rules

The system evaluates rules related to:

```text
Enrollment
Fee Payment
Attendance
Marks
Assignments
Academic Eligibility
Academic Support
Academic Intervention
```

Multiple rules can fire for the same student.

For example:

```text
attendance_low
      ↓
attendance_warning

marks_poor
      ↓
academic_support_required

attendance_warning
+
academic_support_required
      ↓
academic_intervention_required
```

## Versions

### V1

Interactive evaluation of a single student.

### V2

Evaluation of multiple student profiles using the same reusable rule base.

### Learning Focus

- Knowledge representation
- Rule evaluation
- Chained inference
- Decision support
- Explainable reasoning
- Multiple-rule evaluation

---

# 8. Experiment 05 — Missionaries & Cannibals

## Objective

To formulate and solve the classical Missionaries and Cannibals problem using state-space representation, constraints, and BFS.

## State Representation

```text
(Missionaries on Left, Cannibals on Left, Boat Position)
```

Initial state:

```text
(3, 3, L)
```

Goal state:

```text
(0, 0, R)
```

## Constraints

The problem must satisfy:

```text
0 <= M_left <= 3
0 <= C_left <= 3
```

For either bank:

```text
If M > 0:
    M >= C
```

The boat can carry at most two people.

Valid passenger combinations are:

```text
M
MM
C
CC
MC
```

## Versions

### V1

Interactive state-space simulator.

The user selects a boat movement, while the program:

```text
Generate Candidate State
        ↓
Validate State
        ↓
Accept / Reject
        ↓
Goal Test
```

### V2

Automatic BFS-based solver.

The solver:

```text
Initial State
      ↓
Generate Successors
      ↓
Validate States
      ↓
Remove Visited States
      ↓
BFS Queue
      ↓
Goal State
```

The classic problem is solved in:

```text
11 crossings
```

### Learning Focus

- State-space representation
- Constraints
- Successor generation
- Visited-state tracking
- Breadth-First Search
- Shortest-path reasoning
- Goal testing

---

# 9. Concepts Covered Across Lab 1

The experiments collectively cover the core topics of Unit 1.

### AI Problem Formulation

```text
Problem
  ↓
Initial State
  ↓
Actions / Operators
  ↓
State Transitions
  ↓
Goal State
```

### State-Space Representation

Different problems use different state representations:

```text
Water Jug
(Jug1, Jug2)

Vacuum Cleaner
(Room1, Room2, VacuumPosition)

Missionaries & Cannibals
(MissionariesLeft, CannibalsLeft, BoatPosition)
```

### Production Systems

```text
Facts
  +
Rules
  ↓
Inference
  ↓
Derived Knowledge
```

### Constraints

Constraints are used to eliminate invalid states or transitions.

### Goal Testing

Each problem defines a condition under which the problem is considered solved.

### Search

Missionaries & Cannibals introduces automatic state-space exploration using BFS and provides a bridge to the dedicated search algorithms in Lab 2.

---

# 10. Overall Learning Progression

The experiments were intentionally developed in the following progression:

```text
Production Systems
        ↓
Rules + Facts + Inference
        ↓
Water Jug
        ↓
States + Operators + Constraints
        ↓
Vacuum Cleaner
        ↓
State-Based Intelligent Agent
        ↓
Rule-Based Decision Making
        ↓
Knowledge → Decision
        ↓
Missionaries & Cannibals
        ↓
State-Space Search + BFS
```

This progression moves from symbolic reasoning and manual state transitions toward automated problem solving.

---

# 11. Output Artifacts

Each experiment contains its own output artifacts.

Typical structure:

```text
outputs/
├── screenshots/
└── diagrams/
```

State-space diagrams have been created for the major state-space experiments:

```text
02_water_jug/
└── outputs/diagrams/water_jug_state_space.png

03_vacuum_cleaner/
└── outputs/diagrams/vacuum_cleaner_state_space.png

04_rule_based_decision/
└── outputs/diagrams/rule_based_decision_state_space.png

05_missionaries_and_cannibals/
└── outputs/diagrams/missionaries_and_cannibals_state_space.png
```

The screenshots document representative executions, valid and invalid transitions, inference traces, and search results.

---

# 12. Performance and Analysis

Lab 1 primarily focuses on problem formulation and reasoning rather than machine-learning metrics.

Therefore, analysis is based on:

- Number of states
- Number of valid transitions
- Number of invalid transitions
- Number of inference steps
- Number of rules fired
- Number of states explored
- Number of solution steps
- Execution time where relevant
- Solution quality

For the Missionaries & Cannibals BFS solver, the classic problem is solved in **11 crossings**, with BFS providing the shortest solution in terms of number of crossings.

---

# 13. Learning Outcomes

After completing Lab 1, the following concepts were implemented and understood:

- AI problem formulation
- State-space representation
- Initial and goal states
- Operators and actions
- State transitions
- Production systems
- Rule-based reasoning
- Forward chaining
- Backward chaining
- Knowledge representation
- Constraint validation
- Goal testing
- Intelligent agent behavior
- Successor-state generation
- Visited-state tracking
- Breadth-First Search
- Explainable rule-based decisions

---

# 14. Conclusion

Lab 1 established the foundational problem-solving concepts of Artificial Intelligence through classical symbolic and state-space problems.

The experiments progressed from production rules and inference to interactive state-space problems, intelligent-agent behavior, rule-based decision support, and finally automated BFS search.

Together, these experiments provide the foundation for **Lab 2 — Heuristic Search Algorithms**, where BFS, DFS, Hill Climbing, Best First Search, and A* Search will be studied and compared in greater depth.

---

## Lab Status

**Lab 1: ✅ COMPLETED**

**Next:** Lab 2 — Heuristic Search Algorithms
