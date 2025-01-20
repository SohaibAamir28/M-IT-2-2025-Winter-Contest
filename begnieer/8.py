# Second last question: 20/100 for this solution:
def organize_marbles(n, marbles):
    actions = []
    visited = [False] * (n + 1)
    position_map = {marbles[i]: i + 1 for i in range(n)}
    for i in range(1, n + 1):
        if visited[i] or marbles[i - 1] == i:
            continue
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = position_map[current]
        for j in range(len(cycle) - 1):
            actions.append(f"1 {cycle[j]} {cycle[j + 1]}")
    print(len(actions))
    for action in actions:
        print(action)
n = int(input())
marbles = list(map(int, input().split()))
organize_marbles(n, marbles)