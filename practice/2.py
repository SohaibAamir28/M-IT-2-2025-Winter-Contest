def find_takahashi_wins(N, A):
    # Count the number of rounds Takahashi wins
    visited = [False] * (N + 1)
    wins = 0

    for i in range(1, N + 1):
        if not visited[i]:
            # Detect cycle
            cycle = []
            current = i
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = A[current - 1]

            # Check if i exists in the cycle
            if i in cycle:
                wins += 1

    return wins

# Input
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the number of rounds Takahashi wins
result = find_takahashi_wins(N, A)
print(result)
