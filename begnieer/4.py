def valid_ordering(N, K, screenshots):
    # Sort the screenshots lexicographically
    sorted_indices = sorted(range(N), key=lambda i: screenshots[i])
    # Check if the sorted order satisfies the non-decreasing condition
    for j in range(K):  # For each team
        for i in range(1, N):  # Compare consecutive screenshots
            if screenshots[sorted_indices[i - 1]][j] > screenshots[sorted_indices[i]][j]:
                print("NO")
                return
    # If valid, output the sorted order
    print("YES")
    print(" ".join(map(str, [index + 1 for index in sorted_indices])))
# Input Handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    # Read N and K
    N, K = map(int, data[:2])
    # Read screenshots
    screenshots = []
    idx = 2
    for _ in range(N):
        screenshots.append(list(map(int, data[idx:idx + K])))
        idx += K
    valid_ordering(N, K, screenshots)