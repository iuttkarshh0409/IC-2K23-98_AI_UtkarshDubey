graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

start = input("Enter starting node: ").upper()

if start not in graph:
    print("Invalid starting node.")
else:
    queue = [start]
    visited = []

    while queue:
        current = queue.pop(0)

        if current not in visited:
            visited.append(current)
            print("Visiting:", current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

    print("\nBFS Traversal:", " -> ".join(visited))