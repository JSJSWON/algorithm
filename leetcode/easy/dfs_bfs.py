graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# DFS

# 재귀 구조로 구현
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


print(recursive_dfs(1, []))  # [1, 2, 5, 6, 7, 3, 4]


# 스택을 이용해 구현
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


print(iterative_dfs(1))  # [1, 4, 3, 5, 7, 6, 2]


# BFS

# 큐를 이용해 구현
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


print(iterative_bfs(1))  # [1, 2, 3, 4, 5, 6, 7]

# 재귀로는 불가능
