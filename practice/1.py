def flipping_game(n, a):
    # Count the total number of 1s in the array
    total_ones = sum(a)

    # Initialize variables to keep track of the maximum gain
    max_gain = float('-inf')

    # Iterate through all possible subarrays
    for i in range(n):
        for j in range(i, n):
            # Calculate the number of 1s and 0s in the subarray
            ones = sum(a[i:j + 1])
            zeros = (j - i + 1) - ones

            # The gain from flipping this subarray
            gain = zeros - ones

            # Update the maximum gain
            max_gain = max(max_gain, gain)

    # If the array has all 1s, we need to flip at least one segment
    # to fulfill the condition of "exactly one move"
    if total_ones == n:
        return n - 1

    # Return the maximum number of 1s that can be obtained
    return total_ones + max_gain

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
print(flipping_game(n, a))
