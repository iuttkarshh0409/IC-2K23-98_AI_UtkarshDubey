graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

cost = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 5, "E": 2},
    "C": {"F": 3},
    "D": {},
    "E": {"F": 1},
    "F": {}
}

heuristic = {
    "A": 5,
    "B": 3,
    "C": 3,
    "D": 6,
    "E": 1,
    "F": 0
}

start = input("Enter starting node: ").upper()
goal = input("Enter goal node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid starting or goal node.")

else:
    open_list = [start]
    visited = []

    g_score = {}
    g_score[start] = 0

    while open_list:

        best_node = open_list[0]

        for node in open_list:
            current_f = g_score[node] + heuristic[node]
            best_f = g_score[best_node] + heuristic[best_node]

            if current_f < best_f:
                best_node = node

        open_list.remove(best_node)

        if best_node in visited:
            continue

        visited.append(best_node)

        current_f = g_score[best_node] + heuristic[best_node]

        print(
            "Visiting:",
            best_node,
            "| g =",
            g_score[best_node],
            "| h =",
            heuristic[best_node],
            "| f =",
            current_f
        )

        if best_node == goal:
            print("\nGoal reached!")
            print("A* Search:", " -> ".join(visited))
            print("Total cost:", g_score[best_node])
            break

        for neighbour in graph[best_node]:

            new_g = g_score[best_node] + cost[best_node][neighbour]

            if neighbour not in g_score or new_g < g_score[neighbour]:
                g_score[neighbour] = new_g

                if neighbour not in visited and neighbour not in open_list:
                    open_list.append(neighbour)

    else:
        print("\nGoal not reached.")
        print("A* Search:", " -> ".join(visited))