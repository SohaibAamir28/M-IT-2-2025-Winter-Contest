
def number_reduction(N):
    MOD = 10**9 + 7
    primes = [2, 3, 5, 7]

    def dfs(k, valid):
        if k in valid:
            return
        valid.add(k)
        for p in primes:
            if k % p == 0:
                dfs(k // p, valid)

    def count_valid(N):
        valid = set()
        dfs(1, valid)
        count = 0
        for k in range(1, N + 1):
            if all(d not in '23456789' or k % int(d) == 0 for d in str(k)):
                count += 1
        return count

    return count_valid(N)


if __name__ == "__main__":
    N = int(input())
    print(number_reduction(N))
