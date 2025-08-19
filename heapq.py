import heapq

# A* Tree Search Algorithm
def a_star_tree_search(start, goal, successors, heuristic):
    # Open list as a priority queue: (f, g, state, parent)
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start, None))

    # Keep track of parent pointers for reconstructing path
    parents = {}

    while open_list:
        f, g, state, parent = heapq.heappop(open_list)

        # Store parent to rebuild path later
        parents[state] = parent

        # Goal test
        if state == goal:
            # Reconstruct path
            path = []
            node = state
            while node is not None:
                path.append(node)
                node = parents[node]
            return path[::-1], g  # path and total cost

        # Expand node (tree search does not check for duplicates)
        for (child, cost) in successors(state):
            g_new = g + cost
            h = heuristic(child, goal)
            f_new = g_new + h
            heapq.heappush(open_list, (f_new, g_new, child, state))

    return None, float("inf")  # failure


# Example Graph
def successors(state):
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 2), ('D', 5)],
        'B': [('D', 1)],
        'C': [('G', 5)],
        'D': [('G', 2)],
        'G': []
    }
    return graph.get(state, [])


# Heuristic Function
def heuristic(state, goal):
    h_values = {
        'S': 7,
        'A': 6,
        'B': 4,
        'C': 2,
        'D': 1,
        'G': 0
    }
    return h_values.get(state, 0)


# Run the Algorithm
if __name__ == "__main__":
    path, cost = a_star_tree_search('S', 'G', successors, heuristic)
    print("Path found:", path)
    print("Total cost:", cost)
