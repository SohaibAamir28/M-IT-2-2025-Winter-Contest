def bugged_sort(t, test_cases):
    from collections import defaultdict, deque

    results = []

    for n, a, b in test_cases:
        # Create adjacency list for swaps
        adjacency = defaultdict(list)
        for i in range(n):
            adjacency[a[i]].append(b[i])
            adjacency[b[i]].append(a[i])

        # Visited set to mark elements we've processed
        visited = set()

        def bfs(start):
            queue = deque([start])
            component = []
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    queue.extend(neighbor for neighbor in adjacency[current] if neighbor not in visited)
            return component

        # Check all connected components
        possible = True
        for x in range(1, 2 * n + 1):
            if x not in visited:
                component = bfs(x)
                if not is_sortable(component, n):
                    possible = False
                    break

        results.append("YES" if possible else "NO")

    return results

def is_sortable(component, n):
    """ Check if the component can be split into two sorted parts. """
    component.sort()
    # Check if we can split into two halves that can be sorted separately
    return all(1 <= x <= 2 * n for x in component)

# Input Handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    test_cases = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + n]))
        index += n
        test_cases.append((n, a, b))

    results = bugged_sort(t, test_cases)
    sys.stdout.write("\n".join(results) + "\n")
