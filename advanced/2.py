def monster_fighting(n, powers):
    from heapq import heappop, heappush
    type_0, type_1 = [], []

    for p0, p1 in powers:
        heappush(type_0, (-p0, p1))
        heappush(type_1, (-p1, p0))

    for _ in range(n):
        _, weakest = heappop(type_0)
        if not type_1 or weakest < 0:
            return "NO"
        heappop(type_1)

    return "YES"


if __name__ == "__main__":
    n = int(input())
    powers = [tuple(map(int, input().split())) for _ in range(n)]
    print(monster_fighting(n, powers))
