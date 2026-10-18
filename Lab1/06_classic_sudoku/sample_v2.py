
number_book = [1, 2, 3, 4, 5, 6, 7, 8, 9]

playground_location = [
    [1, 1], [1, 2], [1, 3], [1,4], [1,5], [1,6],
    [2, 1], [2, 2], [2, 3], [2,4], [2,5], [2,6],
    [3, 1], [3, 2], [3, 3], [3,4], [3,5], [3,6]
]

assignment_history = []
empty_cells_remaining = 18

while empty_cells_remaining > 0:

    print("\n" + "=" * 35)
    print("       SUDOKU 3x3 BLOCK")
    print("=" * 35)

    print("Available numbers:", number_book)
    print("Empty cells remaining:", empty_cells_remaining)

    # 1. Accept and validate the number
    try:
        number_choice = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input! Enter an integer.")
        continue

    if number_choice not in number_book:
        print("Invalid or already used number! Choose from the available numbers.")
        continue

    # 2. Accept and validate the location
    try:
        location_row = int(input("Enter row (1-6): "))
        location_column = int(input("Enter column (1-3): "))
    except ValueError:
        print("Invalid input! Enter integers.")
        continue

    location_choice = [location_row, location_column]

    if location_choice not in playground_location:
        print("Invalid location! Row and column must be between 1 and 6.")
        continue

    # 3. Check whether the location is occupied
    occupied_locations = [
        entry[1] for entry in assignment_history
    ]

    if location_choice in occupied_locations:
        print("Location already occupied! Choose another location.")
        continue

    # 4. Record the successful assignment
    assignment_history.append([number_choice, location_choice])

    # 5. Update remaining empty cells
    empty_cells_remaining -= 1
 
    print("Assignment successful!")
    print("Current Entries: ",assignment_history)

# 6. Display the completed block
print("\n" + "=" * 35)
print("       COMPLETED SUDOKU BLOCK")
print("=" * 35)

for row in range(1, 7):
    current_row = []

    for column in range(1, 4):
        for entry in assignment_history:
            if entry[1] == [row, column]:
                current_row.append(entry[0])
                break

    print(current_row)

print("\nAll nine cells have been filled successfully!")
print("Final assignment history:", assignment_history)
print("Remaining numbers:", number_book)
