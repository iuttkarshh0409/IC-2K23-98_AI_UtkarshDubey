
# ============================================================
# SUDOKU PROJECT
# Automated Sudoku Solver
# Candidate Generation + Logical Deduction + Backtracking
# ============================================================

from copy import deepcopy

NUMBER_BOOK = set(range(1, 10))


# ============================================================
# 1. ORIGINAL SUDOKU PUZZLE
# ============================================================

original_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

grid = deepcopy(original_grid)

fixed_cells = {
    (r, c)
    for r in range(9)
    for c in range(9)
    if original_grid[r][c] != 0
}


# ============================================================
# 2. STATISTICS
# ============================================================

stats = {
    "naked_singles": 0,
    "hidden_singles": 0,
    "guesses": 0,
    "search_nodes": 0,
    "contradictions": 0
}


# ============================================================
# 3. DISPLAY SUDOKU GRID
# ============================================================

def display_grid(grid):

    print("\n" + "=" * 37)

    for row in range(9):

        if row in (3, 6):
            print("-" * 37)

        for column in range(9):

            if column in (3, 6):
                print("|", end=" ")

            value = grid[row][column]

            print(value if value != 0 else ".", end="  ")

        print()

    print("=" * 37)


# ============================================================
# 4. VALIDATE ORIGINAL PUZZLE
# ============================================================

def is_valid_initial_grid(grid):

    if len(grid) != 9:
        return False

    if any(len(row) != 9 for row in grid):
        return False

    for row in range(9):

        for column in range(9):

            number = grid[row][column]

            if type(number) is not int or number not in range(10):
                return False

            if number == 0:
                continue

            # Check row
            for c in range(9):

                if c != column and grid[row][c] == number:
                    return False

            # Check column
            for r in range(9):

                if r != row and grid[r][column] == number:
                    return False

            # Check 3x3 block
            start_row = (row // 3) * 3
            start_column = (column // 3) * 3

            for r in range(start_row, start_row + 3):

                for c in range(start_column, start_column + 3):

                    if (r, c) != (row, column):
                        if grid[r][c] == number:
                            return False

    return True


# ============================================================
# 5. CANDIDATE GENERATION
# ============================================================

def get_candidates(grid, row, column):

    if grid[row][column] != 0:
        return set()

    used_numbers = set()

    # Collect row numbers
    used_numbers.update(grid[row])

    # Collect column numbers
    for r in range(9):
        used_numbers.add(grid[r][column])

    # Collect 3x3 block numbers
    start_row = (row // 3) * 3
    start_column = (column // 3) * 3

    for r in range(start_row, start_row + 3):

        for c in range(start_column, start_column + 3):

            used_numbers.add(grid[r][c])

    return NUMBER_BOOK - used_numbers


# ============================================================
# 6. DISPLAY CANDIDATES
# ============================================================

def display_candidates(grid):

    print("\nPOSSIBLE CANDIDATES")

    for row in range(9):

        for column in range(9):

            if grid[row][column] == 0:

                candidates = get_candidates(grid, row, column)

                print(
                    f"Cell [{row + 1},{column + 1}] "
                    f"-> {sorted(candidates)}"
                )


# ============================================================
# 7. GENERATE ALL SUDOKU UNITS
# ============================================================

def get_units():

    units = []

    # Nine rows
    for row in range(9):
        units.append([(row, c) for c in range(9)])

    # Nine columns
    for column in range(9):
        units.append([(r, column) for r in range(9)])

    # Nine 3x3 blocks
    for start_row in range(0, 9, 3):

        for start_column in range(0, 9, 3):

            block = []

            for r in range(start_row, start_row + 3):

                for c in range(start_column, start_column + 3):
                    block.append((r, c))

            units.append(block)

    return units


SUDOKU_UNITS = get_units()


# ============================================================
# 8. LOGICAL DEDUCTION ENGINE
# ============================================================

def propagate(grid):

    while True:

        # ------------------------------------------
        # A. NAKED SINGLE DETECTION
        # ------------------------------------------

        for row in range(9):

            for column in range(9):

                if grid[row][column] != 0:
                    continue

                candidates = get_candidates(grid, row, column)

                # No possible candidate means contradiction
                if not candidates:
                    return False

                # Exactly one candidate
                if len(candidates) == 1:

                    number = next(iter(candidates))

                    grid[row][column] = number

                    stats["naked_singles"] += 1

                    # Restart after every assignment
                    break

            else:
                continue

            break

        else:

            # ------------------------------------------
            # B. HIDDEN SINGLE DETECTION
            # ------------------------------------------

            assignment_found = False

            for unit in SUDOKU_UNITS:

                present_numbers = {
                    grid[r][c]
                    for r, c in unit
                    if grid[r][c] != 0
                }

                missing_numbers = NUMBER_BOOK - present_numbers

                for number in missing_numbers:

                    possible_locations = []

                    for r, c in unit:

                        if grid[r][c] == 0:

                            candidates = get_candidates(grid, r, c)

                            if number in candidates:
                                possible_locations.append((r, c))

                    # A missing number has nowhere to go
                    if not possible_locations:
                        return False

                    # Only one possible location
                    if len(possible_locations) == 1:

                        r, c = possible_locations[0]

                        grid[r][c] = number

                        stats["hidden_singles"] += 1

                        assignment_found = True

                        break

                if assignment_found:
                    break

            # No more logical deductions possible
            if not assignment_found:
                return True

        # Restart the deduction process after every assignment


# ============================================================
# 9. FIND CELL WITH MINIMUM REMAINING VALUES (MRV)
# ============================================================

def find_best_cell(grid):

    best_cell = None
    best_candidates = None

    minimum_candidates = 10

    for row in range(9):

        for column in range(9):

            if grid[row][column] != 0:
                continue

            candidates = get_candidates(grid, row, column)

            if len(candidates) < minimum_candidates:

                minimum_candidates = len(candidates)

                best_cell = (row, column)

                best_candidates = candidates

    return best_cell, best_candidates


# ============================================================
# 10. BACKTRACKING SOLVER
# ============================================================

def solve_sudoku(grid):

    stats["search_nodes"] += 1

    # First apply all available logical deductions
    if not propagate(grid):

        stats["contradictions"] += 1

        return None

    # Check whether all cells are filled
    cell, candidates = find_best_cell(grid)

    if cell is None:
        return grid

    row, column = cell

    # Try candidates in ascending order
    for number in sorted(candidates):

        stats["guesses"] += 1

        # Create independent board for this possibility
        new_grid = deepcopy(grid)

        new_grid[row][column] = number

        # Recursively solve
        result = solve_sudoku(new_grid)

        if result is not None:
            return result

    # All possibilities failed
    return None


# ============================================================
# 11. FINAL SOLUTION VALIDATION
# ============================================================

def is_valid_solution(grid):

    # Every row must contain 1-9 exactly once
    for row in range(9):

        if set(grid[row]) != NUMBER_BOOK:
            return False

    # Every column must contain 1-9 exactly once
    for column in range(9):

        current_column = {
            grid[row][column]
            for row in range(9)
        }

        if current_column != NUMBER_BOOK:
            return False

    # Every 3x3 block must contain 1-9 exactly once
    for start_row in range(0, 9, 3):

        for start_column in range(0, 9, 3):

            current_block = set()

            for row in range(start_row, start_row + 3):

                for column in range(start_column, start_column + 3):

                    current_block.add(grid[row][column])

            if current_block != NUMBER_BOOK:
                return False

    # Original clues must remain unchanged
    for row, column in fixed_cells:

        if grid[row][column] != original_grid[row][column]:
            return False

    return True


# ============================================================
# 12. EXECUTION
# ============================================================

print("\n" + "=" * 50)
print("          SUDOKU SOLVER V4.0")
print("=" * 50)

print("\nORIGINAL PUZZLE")
display_grid(grid)

# Validate original puzzle
if not is_valid_initial_grid(grid):

    print("\nInvalid Sudoku puzzle!")
    raise SystemExit

print("\nOriginal puzzle validated successfully.")

print("\nGenerating initial candidates...")
display_candidates(grid)

print("\nStarting logical deduction and backtracking...")

solution = solve_sudoku(deepcopy(grid))


# ============================================================
# 13. FINAL RESULTS
# ============================================================

print("\n" + "=" * 50)
print("                 FINAL RESULTS")
print("=" * 50)

if solution is not None and is_valid_solution(solution):

    print("\nSUDOKU SOLVED SUCCESSFULLY!")

    print("\nSOLVED SUDOKU GRID")
    display_grid(solution)

    print("\nSOLUTION VERIFICATION: PASSED")

    print("All rows: Valid")
    print("All columns: Valid")
    print("All 3x3 blocks: Valid")
    print("Original clues: Preserved")

else:

    print("\nNo valid solution found.")
    print("Puzzle may be unsolvable or inconsistent.")

print("\n" + "=" * 50)
print("             SOLVER STATISTICS")
print("=" * 50)

print("Naked Singles:", stats["naked_singles"])
print("Hidden Singles:", stats["hidden_singles"])
print("Candidate Attempts:", stats["guesses"])
print("Search Nodes:", stats["search_nodes"])
print("Contradictions:", stats["contradictions"])

print("\nSudoku V4.0 execution completed!")
