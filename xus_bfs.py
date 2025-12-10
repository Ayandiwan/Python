from collections import deque

graph = {
    1: [2, 5],
    2: [1, 3, 4],
    3: [2],
    4: [2],
    5: [1, 6],
    6: [5]
}

def bfs(graph, start):
    path = []
    queue = deque([start])

    while queue:
        v = queue.popleft()

        if v not in path:
            path.append(v)
            print("Path:", path)
            queue.extend(graph[v])
            print("Queue:", list(queue))
            print()

    print("Final Path:", path)

bfs(graph, 1)
