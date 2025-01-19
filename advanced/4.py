MOD = 10**9 + 7

def drawing_lines(n, points):
    from collections import defaultdict

    ud_x, lr_y = set(), set()
    for x, y, s in points:
        if s == "UD":
            if x in ud_x:
                return "NO", 0
            ud_x.add(x)
        else:
            if y in lr_y:
                return "NO", 0
            lr_y.add(y)

    count = pow(2, len(ud_x) + len(lr_y), MOD)
    return "YES", count


if __name__ == "__main__":
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        points = [tuple(input().split()) for _ in range(n)]
        points = [(int(x), int(y), s) for x, y, s in points]
        result, count = drawing_lines(n, points)
        results.append((result, count))
    
    for res, cnt in results:
        print(res)
        print(cnt)
