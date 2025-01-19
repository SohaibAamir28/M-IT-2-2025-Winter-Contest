def inverse_knapsack(target):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    MOD = 10**9 + 7

    def crt(a, m):
        M = 1
        for mod in m:
            M *= mod
        result = 0
        for ai, mi in zip(a, m):
            Mi = M // mi
            result += ai * Mi * pow(Mi, -1, mi)
            result %= M
        return result

    coefficients = [128 * target % p for p in primes]
    a_values = [coefficients[i] for i in range(len(primes))]
    result = crt(a_values, primes)
    return result % MOD


if __name__ == "__main__":
    target = int(input())
    print(inverse_knapsack(target))
