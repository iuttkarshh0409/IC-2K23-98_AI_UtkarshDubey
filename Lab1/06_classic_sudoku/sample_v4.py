number_book = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Original Sudoku puzzle
# 0 represents an empty cell

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

# 2. Create a working copy
grid = [row.copy() for row in original_grid]

# 3. Identify immutable prefilled cells
fixed_cells = set()

for row in range(9):
    for column in range(9):

        if original_grid[row][column] != 0:
            fixed_cells.add((row, column))

# 4. Assignment history
assignment_history = []

# 5. Count empty cells
empty_cells_remaining = sum(
    1
    for row in grid
    for value in row
    if value == 0
)


# ==========================================
# DISPLAY FUNCTION
# ==========================================

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


# ==========================================
# INITIAL BOARD DISPLAY
# ==========================================

print("\nINITIAL SUDOKU PUZZLE")
display_grid(grid)

print("\nOriginal clues:", len(fixed_cells))
print("Empty cells:", empty_cells_remaining)


# ==========================================
# MAIN INPUT LOOP
# ==========================================

while empty_cells_remaining > 0:

    print("\nAvailable numbers:", number_book)
    print("Empty cells remaining:", empty_cells_remaining)

    # 6. Accept number
    try:
        number_choice = int(input("\nEnter number (1-9): "))

    except ValueError:
        print("Invalid input! Enter an integer.")
        continue

    if number_choice not in number_book:
        print("Invalid number! Choose between 1 and 9.")
        continue

    # 7. Accept coordinates
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

    row_index = location_row - 1
    column_index = location_column - 1

    location_choice = (row_index, column_index)

    # 8. Protect original clues
    if location_choice in fixed_cells:
        print("This is a prefilled clue! Modification prohibited.")
        continue

    # 9. Check occupied location
    if grid[row_index][column_index] != 0:
        print("Location already occupied!")
        continue

    # 10. Row validation
    if number_choice in grid[row_index]:
        print("Duplicate number in this row!")
        continue

    # 11. Column validation
    duplicate_in_column = any(
        grid[row][column_index] == number_choice
        for row in range(9)
    )

    if duplicate_in_column:
        print("Duplicate number in this column!")
        continue

    # 12. 3x3 block validation
    block_start_row = (row_index // 3) * 3
    block_start_column = (column_index // 3) * 3

    duplicate_in_block = False

    for row in range(block_start_row, block_start_row + 3):

        for column in range(
            block_start_column,
            block_start_column + 3
        ):

            if grid[row][column] == number_choice:
                duplicate_in_block = True
                break

        if duplicate_in_block:
            break

    if duplicate_in_block:
        print("Duplicate number in this 3x3 block!")
        continue

    # 13. Successful assignment
    grid[row_index][column_index] = number_choice

    assignment_history.append([
        number_choice,
        location_choice
    ])

    empty_cells_remaining -= 1

    print("\nAssignment successful!")
    display_grid(grid)


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\nSUDOKU BOARD COMPLETED")
display_grid(grid)

print("\nTotal original clues:", len(fixed_cells))
print("Total user assignments:", len(assignment_history))
print("Remaining empty cells:", empty_cells_remaining)
