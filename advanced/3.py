def lis_possible(n, k, arr):
    from bisect import bisect_left

    def lis_length(sequence):
        lis = []
        for x in sequence:
            pos = bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        return len(lis)

    lis = lis_length(arr)
    if lis + k - n <= (k + 1) // 2:
        return "YES"
    return "NO"


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(lis_possible(n, k, arr))
