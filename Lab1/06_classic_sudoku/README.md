# Sudoku Solver: From Logical Deduction to Algorithmic Problem Solving

**Project:** Classic Sudoku Solver  
**Language:** Python  
**Latest Implementation:** `sample_v6.py`  
**Problem Domain:** Constraint Satisfaction, Logical Deduction, Recursive Backtracking

---

## 1. About the Project

This project explores the implementation of a classic 9×9 Sudoku system through a progressive, logic-driven programming approach.

Rather than immediately implementing a conventional Sudoku-solving algorithm, the development started with a much simpler question:

**How can a program systematically assign numbers to a collection of cells while ensuring that no assignment violates the established rules?**

The initial approach focused on representing numbers, cell coordinates, assignment history, and validation conditions. Gradually, this small assignment mechanism evolved into a complete Sudoku representation, a constraint-validation system, and eventually an automated solving engine.

The project demonstrates the progression from basic data structures and conditional logic to constraint propagation, candidate elimination, heuristic selection, and recursive backtracking.

The objective was not simply to obtain a solved Sudoku grid, but to understand and implement the reasoning process behind solving one.

---

## 2. The Development Philosophy

The project follows a bottom-up development strategy.

Instead of starting with the complete 9×9 problem, the initial implementation deliberately restricted its scope to a single 3×3 block.

This allowed the fundamental concepts to be understood independently:

- Representing numbers and their possible locations.
- Managing assignments through a structured data collection.
- Preventing duplicate number assignments.
- Preventing multiple assignments to the same location.
- Tracking the remaining unoccupied cells.
- Introducing progressively more complex validation conditions.

Once the basic assignment mechanism was established, the scope expanded to multiple blocks and eventually the complete Sudoku grid.

The central philosophy throughout development was:

**Understand the problem, establish its constraints, represent its state, and progressively automate the reasoning process.**

---

## 3. Development Journey and Version Progression

The following progression describes the major conceptual stages of the project, from the initial prototype to the automated solver.

### Stage 1: Basic 3×3 Block Assignment

The first implementation focused exclusively on a single 3×3 Sudoku block.

The problem was represented using two primary data structures:

- `number_book`: A collection containing numbers from 1 to 9.
- `playground_location`: A collection of nine coordinate pairs representing the available cells.

An assignment history was introduced to record which number had been placed at which coordinate.

**Core implementation concepts:**

- List-based data representation.
- Two-dimensional coordinate representation.
- User-driven number selection.
- Assignment history.
- Duplicate number detection.
- Occupied location detection.
- Remaining empty-cell tracking.

The program accepted a number and a coordinate, validated the assignment, and recorded it only when both were valid.

The first important design decision was to reject invalid assignments rather than automatically modify the user's selection.

This established the basic validation-before-assignment mechanism.

### Stage 2: Expanding the Playground

After establishing the single-block assignment mechanism, the scope was expanded to accommodate multiple adjacent 3×3 blocks.

The playground was extended to represent six rows and three columns, allowing the first two blocks of the upper Sudoku region to be considered together.

This introduced an important new constraint:

**A number that is unique within an individual block may still violate the uniqueness requirement of a shared row.**

Consequently, row-level validation became necessary.

Another important design decision was to retain the original `number_book` rather than removing previously selected numbers from it.

This separated the original collection of possible values from the assignment history and allowed validation to determine whether a number had already been used.

**Core concepts introduced:**

- Expanded coordinate space.
- Row-level uniqueness.
- Assignment validation across multiple blocks.
- Separation of available numbers and assignment history.

### Stage 3: Complete 9×9 Grid Representation

The next major progression was the transition from isolated blocks to a complete Sudoku board.

Instead of representing only the active playground, the program introduced a complete 9×9 two-dimensional list.

The board became the central representation of the puzzle.

The initial puzzle was loaded with prefilled values, while empty cells were represented using `0`.

This introduced two important concepts.

**Original puzzle preservation**

The original grid was maintained separately from the working grid. A copy was used for subsequent assignments.

**Immutable prefilled clues**

The coordinates of originally populated cells were recorded separately.

This allowed the program to distinguish between:

- Original clues supplied by the puzzle.
- New assignments introduced during execution.

Original clues were protected from modification.

The empty-cell count was also calculated dynamically instead of relying on a hardcoded value.

**Core concepts introduced:**

- Complete 9×9 matrix representation.
- Original puzzle initialization.
- Working-copy management.
- Immutable prefilled cells.
- Assignment history.
- Dynamic empty-cell counting.

### Stage 4: Centralized Constraint Validation

As the board expanded, maintaining individual validation conditions inside the main input loop became increasingly inconvenient.

The validation logic was therefore consolidated into reusable functions.

The three fundamental Sudoku constraints were implemented:

1. **Row constraint:** A number cannot appear more than once in the same row.
2. **Column constraint:** A number cannot appear more than once in the same column.
3. **3×3 block constraint:** A number cannot appear more than once in the same 3×3 block.

A centralized validation function made it possible to check an assignment using its row, column, and proposed number.

Additional functions were introduced for:

- Initial puzzle validation.
- Board completeness checking.
- Final solution verification.
- Grid display.

This separated input handling, validation, and board verification into independent responsibilities.

**Core concepts introduced:**

- Functional decomposition.
- Reusable validation logic.
- Initial puzzle integrity checking.
- Final board verification.
- Separation of concerns.

### Stage 5: Automated Candidate Generation and Logical Deduction

The next major conceptual shift was moving from manual number assignment to automated reasoning.

Instead of asking the user which number should occupy a particular cell, the program began calculating the possible candidates for every empty cell.

For an empty cell, the candidate set is determined by eliminating all numbers already present in its corresponding row, column, and 3×3 block.

Conceptually:

`Candidates = {1, 2, ..., 9} - (Row ∪ Column ∪ Block)`

Two logical deduction techniques were introduced.

**Naked Singles**

When an empty cell has exactly one possible candidate, that candidate must occupy the cell.

**Hidden Singles**

When a number can occupy only one possible position within a particular row, column, or 3×3 block, that position must contain the number.

The deduction process repeatedly applies these techniques until no further forced assignments can be identified.

This established the foundation of an automated logical solving engine.

### Stage 6: Heuristic Search and Recursive Backtracking

Logical deductions alone are not sufficient to solve every valid Sudoku puzzle.

To handle situations where the program reaches a point with no further forced deductions, recursive backtracking was introduced.

The solver selects an unresolved cell, tries one of its possible candidates, and recursively explores the resulting board.

If a contradiction is encountered, the current possibility is abandoned and another candidate is explored.

The Minimum Remaining Values (MRV) heuristic improves this process.

Instead of selecting an arbitrary empty cell, the algorithm selects the cell with the fewest remaining candidates.

This reduces unnecessary branching and prioritizes the most constrained decisions.

**Core concepts introduced:**

- Recursive problem solving.
- Backtracking.
- Contradiction detection.
- Minimum Remaining Values heuristic.
- Independent board states for search branches.
- Automated solution verification.

The culmination of this progression is represented by `sample_v6.py`.

---

## 4. The Core Architecture

The project progressively developed around a collection of complementary data structures and functions.

### Important Data Structures

| Structure | Responsibility |
|---|---|
| `number_book` | Represents the possible Sudoku values, 1–9. |
| `playground_location` | Represents the coordinates available for assignment. |
| `grid` | Stores the current 9×9 Sudoku board. |
| `original_grid` | Preserves the original puzzle. |
| `fixed_cells` | Identifies immutable prefilled clues. |
| `assignment_history` | Records user-created assignments. |
| `empty_cells_remaining` | Tracks unoccupied cells during manual assignment. |
| Candidate sets | Represent possible values for individual empty cells. |

### Major Functional Components

The automated implementation separates responsibilities into functions such as:

- `display_grid()`
- `is_valid_move()`
- `is_valid_initial_grid()`
- `get_candidates()`
- `display_candidates()`
- `get_units()`
- `propagate()`
- `find_best_cell()`
- `solve_sudoku()`
- `is_board_complete()`
- `is_valid_solution()`

Together, these components establish a modular structure for representing, validating, analyzing, and solving Sudoku puzzles.

---

## 5. Algorithmic Concepts Explored

This project provides practical exposure to several important programming and algorithmic concepts.

| Concept | Application |
|---|---|
| Arrays and Lists | Representing numbers, coordinates, and assignments. |
| Two-Dimensional Arrays | Representing the Sudoku board. |
| Sets | Managing candidate numbers and detecting duplicates. |
| Conditional Logic | Enforcing Sudoku constraints. |
| Iteration | Traversing rows, columns, and blocks. |
| Functions | Separating validation and solving responsibilities. |
| Recursion | Exploring alternative Sudoku configurations. |
| Backtracking | Recovering from contradictory assignments. |
| Heuristics | Selecting the most constrained empty cell. |
| Constraint Satisfaction | Modelling Sudoku as a collection of interacting restrictions. |

---

## 6. The Distinctive Approach

An important aspect of this project is its development methodology.

The implementation did not begin with recursion, backtracking, or an existing Sudoku-solving algorithm.

It began with a manually controlled assignment system.

The initial abstraction was straightforward:

- A number must be selected.
- A location must be selected.
- The assignment must be validated.
- The assignment must be recorded.
- The remaining work must be updated.

This small mechanism provided the foundation for progressively introducing more complex constraints.

The development followed a deliberate progression:

**Assignment → Validation → State Management → Constraint Representation → Logical Deduction → Heuristic Search → Automated Solving**

This approach made it possible to understand the relationship between individual Sudoku rules and the algorithms eventually required to solve the complete puzzle.

Rather than treating Sudoku as a problem that simply requires finding the correct final arrangement, the project approaches it as a sequence of decisions that must remain consistent with the state of the entire board.

---

## 7. Current Project Capabilities

The latest implementation, `sample_v6.py`, represents the automated solving stage.

Its intended capabilities include:

- Loading a complete 9×9 Sudoku puzzle.
- Preserving original prefilled clues.
- Validating the initial puzzle.
- Generating candidates for empty cells.
- Applying Naked Single deductions.
- Applying Hidden Single deductions.
- Identifying contradictions.
- Selecting constrained cells through MRV.
- Exploring candidate assignments recursively.
- Backtracking when a candidate leads to a contradiction.
- Verifying the resulting solution against all Sudoku constraints.

The implementation returns the first valid solution it discovers. It does not currently establish whether the original puzzle has exactly one solution or enumerate every possible solution.

---

## 8. Running the Project

Ensure Python 3 is installed.

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <repository-directory>
```

Run the latest implementation:

```bash
python sample_v6.py
```

No third-party packages are required for the core implementation. The solver uses Python's standard library.

---

## 9. Learning Outcomes

Through this project, the development explored:

1. Converting a real-world puzzle into a structured computational representation.
2. Breaking a complex problem into smaller, manageable components.
3. Designing validation rules before implementing automated decisions.
4. Maintaining consistency between the original puzzle and its working state.
5. Representing possibilities through candidate sets.
6. Applying logical deduction to reduce the search space.
7. Understanding recursive search and backtracking.
8. Using heuristics to improve search efficiency.
9. Separating problem representation, validation, and solving into independent components.

---

## 10. Future Scope

Although the current implementation provides an automated Sudoku-solving engine, several improvements can extend its capabilities.

Potential future enhancements include:

- Naked Pairs and Triples.
- Hidden Pairs and Triples.
- Pointing Pairs and Box-Line Reduction.
- X-Wing and other advanced logical techniques.
- Solution uniqueness detection.
- Multiple-solution enumeration.
- Search-performance benchmarking.
- Difficulty estimation based on required solving techniques.
- Interactive Sudoku interface.
- Step-by-step explanation of every deduction.
- Visualization of candidate elimination and backtracking.

These enhancements could transform the current solver into an interactive Sudoku reasoning and analysis platform.

---

## 11. Conclusion

What began as an experiment involving nine numbers and nine coordinate pairs gradually evolved into an automated constraint-based solving system.

The project demonstrates how a complex problem can be approached incrementally by understanding its fundamental rules, designing suitable data structures, introducing validation mechanisms, and progressively automating the decision-making process.

The most important outcome is not merely the ability to generate a completed Sudoku grid.

It is the progression of the underlying problem-solving approach:

**Start with a small, understandable problem. Build a reliable representation. Introduce constraints. Automate the reasoning. Expand only when the existing abstraction is understood.**

That progression is the central idea behind this project.

---

**Project Status:** Automated Sudoku Solver — `sample_v6.py`  
**Language:** Python  
**Approach:** Logic-driven, constraint-based, recursive search and backtracking.
