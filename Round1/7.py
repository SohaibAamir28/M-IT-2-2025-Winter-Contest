def solve_bugged_sort(t, test_cases):
    results = []

    for n, a, b in test_cases:
        # Create a union-find structure
        parent = list(range(2 * n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Connect a[i] and b[i] in the union-find structure
        for i in range(n):
            union(a[i], b[i])

        # Group elements by their root
        components = {}
        for x in a + b:
            root = find(x)
            if root not in components:
                components[root] = []
            components[root].append(x)

        # Check if each component can be sorted
        valid = True
        for component in components.values():
            component.sort()
            if component != sorted(component):
                valid = False
                break

        results.append("YES" if valid else "NO")
    
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Solve and output results
results = solve_bugged_sort(t, test_cases)
print("\n".join(results))
