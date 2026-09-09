start = int(input("Enter start value: "))
end = int(input("Enter end value: "))
target = int(input("Enter target value: "))

found = False

for i in range(start, end + 1):
    print("Testing:", i)

    if i == target:
        print(target, "is found...")
        print("Search successful...")
        found = True
        break

if not found:
    print(target, "is not found...")
    print("Search failed...")