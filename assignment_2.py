
import heapq

def astar(graph, start, goal, h):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                heapq.heappush(
                    queue, (new_f, new_g, neighbor,
                            path + [neighbor])
                )

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

h = {
    'A': 6, 'B': 5, 'C': 3,
    'D': 4, 'E': 2, 'F': 1, 'G': 0
}

path, cost = astar(graph, 'A', 'G', h)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)
