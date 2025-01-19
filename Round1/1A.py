def max_fibonacciness(t, test_cases):
    results = []
    for case in test_cases:
        a1, a2, a4, a5 = case
        max_fibo = 0

        # Iterate over all possible values of a3
        for a3 in range(-200, 201):  # Considering the range for potential a3 values
            count = 0

            # Check conditions for Fibonacciness
            if a1 + a2 == a3:
                count += 1
            if a2 + a3 == a4:
                count += 1
            if a3 + a4 == a5:
                count += 1

            # Update maximum Fibonacciness
            max_fibo = max(max_fibo, count)

        results.append(max_fibo)
    
    return results

# Input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [list(map(int, line.split())) for line in data[1:]]

# Output
results = max_fibonacciness(t, test_cases)
print("\n".join(map(str, results)))
