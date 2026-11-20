from collections import deque

def find_pair(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return i, j

    return None

graph = [
    [1, 2],  # 0번과 연결된 노드
    [0, 3],  # 1번과 연결된 노드
    [0],     # 2번과 연결된 노드
    [1],     # 3번과 연결된 노드
]

def dfs(graph, start):
    visited = {start}
    stack = [start]

    while stack:
        node = stack.pop()

        for nxt in graph[node]:
            if nxt in visited:
                continue

            visited.add(nxt)
            stack.append(nxt)

    return visited

print(dfs(graph, 0))  # {0, 1, 2, 3}

def bfs(graph, start):
    distance = [-1] * len(graph)
    distance[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for nxt in graph[node]:
            if distance[nxt] != -1:
                continue

            distance[nxt] = distance[node] + 1
            queue.append(nxt)

    return distance

def bfs_grid(board, start):
    rows, cols = len(board), len(board[0])
    distance = [[-1] * cols for _ in range(rows)]

    sr, sc = start
    if board[sr][sc] == 1:
        return distance

    queue = deque([(sr, sc)])
    distance[sr][sc] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if board[nr][nc] == 1:
                continue
            if distance[nr][nc] != -1:
                continue

            distance[nr][nc] = distance[r][c] + 1
            queue.append((nr, nc))

    return distance

def permutations(n, m):
    result = []
    path = []
    used = [False] * (n + 1)

    def search():
        if len(path) == m:
            result.append(path.copy())
            return

        for num in range(1, n + 1):
            if used[num]:
                continue

            used[num] = True
            path.append(num)

            search()

            path.pop()
            used[num] = False

    search()
    return result

def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

arr = [1, 3, 3, 7]

idx = lower_bound(arr, 3)  # 1

if idx < len(arr) and arr[idx] == 3:
    print("존재")

def first_possible(low, high, possible):
    # 전제:
    # possible(x)가 False ... False, True ... True 형태
    # high는 반드시 가능한 값
    while low < high:
        mid = (low + high) // 2

        if possible(mid):
            high = mid
        else:
            low = mid + 1

    return low

import heapq

def dijkstra(graph, start):
    distance = [float("inf")] * len(graph)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if cost > distance[node]:
            continue

        for nxt, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))

    return distance

"""
전부 확인해도 입력 크기를 감당할 수 있나? → 완전탐색
연결된 곳을 찾아야 하나? → DFS 또는 BFS
최단거리인가? → 비용이 같으면 BFS, 다르면 다익스트라 검토
선택의 모든 경우를 만들어야 하나? → 백트래킹
답의 경계 전후로 가능 여부가 한 번만 바뀌나? → 이분탐색
"""