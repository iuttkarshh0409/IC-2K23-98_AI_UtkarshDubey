number_book = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Initialize 9x9 Sudoku grid
grid = [[0 for _ in range(9)] for _ in range(9)]

# 2. Prefilled top-left 3x3 block
prefilled_block = [
    [4, 7, 2],
    [8, 1, 5],
    [3, 9, 6]
]

for row in range(3):
    for column in range(3):
        grid[row][column] = prefilled_block[row][column]

# 3. Define top-right block locations
playground_location = [
    [row, column]
    for row in range(1, 4)
    for column in range(7, 10)
]

# 4. Initialize assignment tracking
assignment_history = []
empty_cells_remaining = 9


# ==========================================
# DISPLAY FUNCTION
# ==========================================

def display_grid(grid):

    print("\nCurrent Sudoku Grid:")
    print("-" * 37)

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

    print("-" * 37)


# ==========================================
# MAIN PROGRAM
# ==========================================

while empty_cells_remaining > 0:

    print("\n" + "=" * 40)
    print("       SUDOKU")
    print("       TOP-RIGHT BLOCK")
    print("=" * 40)

    print("Available numbers:", number_book)
    print("Empty cells remaining:", empty_cells_remaining)

    # 5. Accept number input
    try:
        number_choice = int(input("\nEnter a number (1-9): "))

    except ValueError:
        print("Invalid input! Enter an integer.")
        continue

    if number_choice not in number_book:
        print("Invalid number! Choose from 1 to 9.")
        continue

    # 6. Accept location input
    try:
        location_row = int(input("Enter row (1-3): "))
        location_column = int(input("Enter column (7-9): "))

    except ValueError:
        print("Invalid input! Enter integers.")
        continue

    location_choice = [location_row, location_column]

    if location_choice not in playground_location:
        print("Invalid location!")
        print("Use rows 1-3 and columns 7-9.")
        continue

    row_index = location_row - 1
    column_index = location_column - 1

    # 7. Occupied location validation
    if grid[row_index][column_index] != 0:
        print("Location already occupied!")
        continue

    # 8. Row validation
    duplicate_in_row = False

    for column in range(9):

        if grid[row_index][column] == number_choice:
            duplicate_in_row = True
            break

    if duplicate_in_row:
        print("Duplicate number in this row!")
        continue

    # 9. Column validation
    duplicate_in_column = False

    for row in range(9):

        if grid[row][column_index] == number_choice:
            duplicate_in_column = True
            break

    if duplicate_in_column:
        print("Duplicate number in this column!")
        continue

    # 10. 3x3 block validation
    duplicate_in_block = False

    block_start_row = (row_index // 3) * 3
    block_start_column = (column_index // 3) * 3

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

    # 11. Record successful assignment
    assignment_history.append([
        number_choice,
        location_choice
    ])

    grid[row_index][column_index] = number_choice

    # 12. Update remaining cells
    empty_cells_remaining -= 1

    print("\nAssignment successful!")

    print("Current assignment history:")
    print(assignment_history)

    display_grid(grid)


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n" + "=" * 40)
print("       TOP-RIGHT BLOCK COMPLETED")
print("=" * 40)

display_grid(grid)

print("\nFinal Assignment History:")
print(assignment_history)

print("\nEmpty cells remaining:", empty_cells_remaining)

print("\nSudoku execution completed!")
