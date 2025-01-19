MOD = 998244353

def precompute_divisors(k):
    divisors = [[] for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(i, k + 1, i):
            divisors[j].append(i)
    return divisors

def geometric_series_sum(base, length, mod):
    if length == 0:
        return 0
    if base == 1:
        return length % mod
    numerator = pow(base, length, mod) - 1
    denominator = pow(base - 1, mod - 2, mod)
    return (numerator * denominator) % mod

def solve_multiplicative_arrays(t, test_cases):
    max_k = max(tc[0] for tc in test_cases)
    divisors = precompute_divisors(max_k)
    results = []
    
    for k, n in test_cases:
        dp = [0] * (k + 1)
        dp[1] = 1
        
        for x in range(2, k + 1):
            dp[x] = 1  # Count the array [x]
            for d in divisors[x]:
                if d < x:
                    dp[x] = (dp[x] + dp[d]) % MOD
        
        result = []
        for x in range(1, k + 1):
            if n <= 1:
                result.append(dp[x])
            else:
                total = geometric_series_sum(dp[x], n, MOD)
                result.append(total)
        
        results.append(result)
    
    return results

# Input Handling
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Solve and Output
results = solve_multiplicative_arrays(t, test_cases)
for res in results:
    print(" ".join(map(str, res)))
