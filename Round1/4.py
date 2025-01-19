def is_non_decreasing(t, test_cases):
    results = []
    
    for n, a in test_cases:
        possible = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                possible = False
                break
        results.append("YES" if possible else "NO")
    
    return results

# Input Handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Solve
results = is_non_decreasing(t, test_cases)

# Output Results
print("\n".join(results))
