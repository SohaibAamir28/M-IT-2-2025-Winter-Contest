def game_of_mathletes(t, test_cases):
    results = []
    
    for case in test_cases:
        n, k = case[0]
        x = sorted(case[1])
        
        i, j = 0, n - 1
        score = 0
        
        while i < j:
            if x[i] + x[j] == k:
                score += 1
                i += 1
                j -= 1
            elif x[i] + x[j] < k:
                i += 1
            else:
                j -= 1
        
        results.append(score)
    
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    test_cases.append(((n, k), x))

# Solve and Output
results = game_of_mathletes(t, test_cases)
for res in results:
    print(res)
