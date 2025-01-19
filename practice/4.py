import sys
from collections import defaultdict
import heapq

def max_social_distance(N, M, edges):
    def is_valid(X):
        colors = [-1] * (N + 1)

        def dfs(node, color):
            colors[node] = color
            for neighbor, weight in graph[node]:
                if weight < X:
                    continue
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True

        for i in range(1, N + 1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    left, right = 1, max(w for _, _, w in edges)
    result = 1
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Input
input = sys.stdin.read
lines = input().splitlines()
N, M = map(int, lines[0].split())
edges = [tuple(map(int, line.split())) for line in lines[1:]]

# Calculate and print the maximum social distance
print(max_social_distance(N, M, edges))
