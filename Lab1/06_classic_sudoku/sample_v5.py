
# ==================================================
# SUDOKU 
# Centralized Validation + Board Integrity Checker
# ==================================================

number_book = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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

# 2. Create working grid
grid = [row.copy() for row in original_grid]

# 3. Identify immutable clues
fixed_cells = set()

for row in range(9):
    for column in range(9):
        if original_grid[row][column] != 0:
            fixed_cells.add((row, column))

# 4. Assignment tracking
assignment_history = []

# 5. Count empty cells
empty_cells_remaining = sum(
    1 for row in grid for value in row if value == 0
)


# ==================================================
# FUNCTION 1: DISPLAY GRID
# ==================================================

def display_grid(grid):

    print("\n" + "=" * 37)

    for row in range(9):

        if row in [3, 6]:
            print("-" * 37)

        for column in range(9):

            if column in [3, 6]:
                print("|", end=" ")

            value = grid[row][column]

            if value == 0:
                print(".", end="  ")
            else:
                print(value, end="  ")

        print()

    print("=" * 37)


# ==================================================
# FUNCTION 2: VALIDATE A MOVE
# ==================================================

def is_valid_move(grid, row, column, number):

    # Validate row
    for col in range(9):

        if col != column and grid[row][col] == number:
            return False

    # Validate column
    for r in range(9):

        if r != row and grid[r][column] == number:
            return False

    # Identify corresponding 3x3 block
    block_start_row = (row // 3) * 3
    block_start_column = (column // 3) * 3

    # Validate 3x3 block
    for r in range(block_start_row, block_start_row + 3):

        for c in range(block_start_column, block_start_column + 3):

            if (r, c) != (row, column):
                if grid[r][c] == number:
                    return False

    return True


# ==================================================
# FUNCTION 3: VALIDATE ORIGINAL PUZZLE
# ==================================================

def is_valid_initial_grid(grid):

    for row in range(9):

        for column in range(9):

            number = grid[row][column]

            if number == 0:
                continue

            if number not in number_book:
                return False

            if not is_valid_move(grid, row, column, number):
                return False

    return True


# ==================================================
# FUNCTION 4: CHECK WHETHER BOARD IS COMPLETE
# ==================================================

def is_board_complete(grid):

    for row in range(9):

        for column in range(9):

            if grid[row][column] == 0:
                return False

    return True


# ==================================================
# FUNCTION 5: VERIFY COMPLETE SUDOKU SOLUTION
# ==================================================

def is_valid_solution(grid):

    expected = number_book

    # Check all rows
    for row in range(9):

        if sorted(grid[row]) != expected:
            return False

    # Check all columns
    for column in range(9):

        current_column = [
            grid[row][column]
            for row in range(9)
        ]

        if sorted(current_column) != expected:
            return False

    # Check all nine 3x3 blocks
    for block_row in range(0, 9, 3):

        for block_column in range(0, 9, 3):

            current_block = []

            for row in range(block_row, block_row + 3):

                for column in range(block_column, block_column + 3):

                    current_block.append(grid[row][column])

            if sorted(current_block) != expected:
                return False

    return True


# ==================================================
# INITIAL PUZZLE VALIDATION
# ==================================================

print("\nSUDOKU V3.4 INITIALIZATION")

if not is_valid_initial_grid(grid):

    print("ERROR: Original puzzle contains conflicting clues.")
    raise SystemExit

print("Original puzzle validated successfully!")

print("Original clues:", len(fixed_cells))
print("Empty cells:", empty_cells_remaining)

display_grid(grid)


# ==================================================
# MAIN PROGRAM
# ==================================================

while empty_cells_remaining > 0:

    print("\n" + "=" * 40)
    print("          SUDOKU V3.4")
    print("=" * 40)

    print("Available numbers:", number_book)
    print("Empty cells remaining:", empty_cells_remaining)

    # Accept number
    try:
        number_choice = int(input("\nEnter number (1-9): "))

    except ValueError:
        print("Invalid input! Enter an integer.")
        continue

    if number_choice not in number_book:
        print("Invalid number! Choose between 1 and 9.")
        continue

    # Accept coordinates
    try:
        location_row = int(input("Enter row (1-9): "))
        location_column = int(input("Enter column (1-9): "))

    except ValueError:
        print("Invalid coordinates!")
        continue

    if not (1 <= location_row <= 9 and
            1 <= location_column <= 9):

        print("Coordinates must be between 1 and 9.")
        continue

    # Convert to zero-based indexing
    row_index = location_row - 1
    column_index = location_column - 1

    location_choice = (row_index, column_index)

    # Check fixed clue protection
    if location_choice in fixed_cells:
        print("Original clue cannot be modified!")
        continue

    # Check occupied location
    if grid[row_index][column_index] != 0:
        print("Location already occupied!")
        continue

    # Centralized move validation
    if not is_valid_move(
        grid,
        row_index,
        column_index,
        number_choice
    ):

        print("INVALID MOVE!")
        print("Row, column or 3x3 block constraint violated.")
        continue

    # Record successful assignment
    grid[row_index][column_index] = number_choice

    assignment_history.append([
        number_choice,
        location_choice
    ])

    empty_cells_remaining -= 1

    print("\nAssignment successful!")

    display_grid(grid)


# ==================================================
# FINAL BOARD INTEGRITY CHECK
# ==================================================

print("\n" + "=" * 40)
print("       FINAL BOARD VERIFICATION")
print("=" * 40)

display_grid(grid)

if is_board_complete(grid):

    print("Board completeness: PASSED")

    if is_valid_solution(grid):

        print("Row validation: PASSED")
        print("Column validation: PASSED")
        print("3x3 block validation: PASSED")

        print("\nSUDOKU SOLVED SUCCESSFULLY!")

    else:

        print("\nBOARD INTEGRITY CHECK FAILED!")

else:

    print("Board is incomplete.")

print("\nOriginal clues:", len(fixed_cells))
print("User assignments:", len(assignment_history))
print("Empty cells:", empty_cells_remaining)

print("\nAssignment history:")
print(assignment_history)
