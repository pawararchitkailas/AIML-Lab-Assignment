from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

visited = []
queue = deque()

start = 'A'

visited.append(start)
queue.append(start)

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
            