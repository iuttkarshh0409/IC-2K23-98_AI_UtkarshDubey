def function(x):
    return -(x - 5) ** 2 + 25


start = int(input("Enter starting value: "))

current = start

while True:
    current_value = function(current)

    left = current - 1
    right = current + 1

    left_value = function(left)
    right_value = function(right)

    print("\nCurrent:", current, "Value:", current_value)
    print("Left:", left, "Value:", left_value)
    print("Right:", right, "Value:", right_value)

    if left_value > current_value:
        current = left

    elif right_value > current_value:
        current = right

    else:
        print("\nLocal maximum reached.")
        print("Best state:", current)
        print("Best value:", current_value)
        break