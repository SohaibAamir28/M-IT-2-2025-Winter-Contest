def find_interesting_subsequence(T, test_cases):
    results = []

    for n, k, a in test_cases:
        # We take the first K elements (indices) from the sorted array
        indices = sorted(range(n), key=lambda x: a[x])[:k]
        indices.sort()  # Sort the indices to maintain subsequence order

        # Verify the longest increasing subsequence condition
        subsequence = [a[i] for i in indices]
        lis_length = 1
        current_max = subsequence[0]
        for value in subsequence[1:]:
            if value > current_max:
                lis_length += 1
                current_max = value

        if lis_length <= (k + 1) // 2:
            results.append(("YES", [i + 1 for i in indices]))
        else:
            results.append(("NO", []))

    return results

# Input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, k = map(int, data[index].split())
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, k, a))
    index += 2

# Output
results = find_interesting_subsequence(t, test_cases)
for result in results:
    if result[0] == "YES":
        print("YES")
        print(" ".join(map(str, result[1])))
    else:
        print("NO")