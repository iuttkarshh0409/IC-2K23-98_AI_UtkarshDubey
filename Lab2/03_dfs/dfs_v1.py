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
    stack = [start]
    visited = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)
            print("Visiting:", current)

            for neighbour in reversed(graph[current]):
                if neighbour not in visited:
                    stack.append(neighbour)

    print("\nDFS Traversal:", " -> ".join(visited))