graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

heuristic = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 7,
    "E": 3,
    "F": 0
}

start = input("Enter starting node: ").upper()
goal = input("Enter goal node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid starting or goal node.")

else:
    open_list = [start]
    visited = []

    while open_list:

        best_node = open_list[0]

        for node in open_list:
            if heuristic[node] < heuristic[best_node]:
                best_node = node

        open_list.remove(best_node)

        if best_node not in visited:
            visited.append(best_node)
            print("Visiting:", best_node)

            if best_node == goal:
                print("\nGoal reached!")
                print("Best First Search:", " -> ".join(visited))
                break

            for neighbour in graph[best_node]:
                if neighbour not in visited and neighbour not in open_list:
                    open_list.append(neighbour)

    else:
        print("\nGoal not reached.")
        print("Best First Search:", " -> ".join(visited))