from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)



# def bfs():
#     dq = deque()
#     dq.append(0)

#     while dq:
#         now = dq.popleft()
#         for nxt in range(13):
#             if adj[now][nxt]:
#                 dq.append(nxt)

# visited = [False] * (len(graph) - 1)

# def bfs(start):
#     dq = deque()
#     dq.append(start)

#     while dq:
#         now = dq.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 dq.append(i)
        



graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 

# def dfs(graph, start, visited):
#     visited[start] = True
#     print(start, end=' ')
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)


def bfs(graph, start, visited):
    dq = deque([start])
    visited[start] = True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True


bfs(graph, 1, visited)