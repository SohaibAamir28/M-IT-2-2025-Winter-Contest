import sys
input = sys.stdin.readline
def is_repetitive(s):
    n = len(s)
    i = 0
    while i < n:
        if s[i] != 'M':
            return False
        i += 1
        if i >= n or s[i] != 'I':
            return False
        i += 1
        if i >= n or s[i] != 'T':
            return False
        i += 1
        while i < n - 1 and s[i] == 'I' and s[i + 1] == 'T':
            i += 2
    return i == n
def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        n = int(input().strip())
        s = input().strip()
        results.append("YES" if is_repetitive(s) else "NO")
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()

#     Problem # 2 solution in Python M(IT)+
# def is_repetitive_string(s):
#     i = 0
#     n = len(s)
#     while i < n:
#         if s[i] == 'M':
#             i += 1
#             if i < n and s[i:i+2] == 'IT':
#                 while i + 1 < n and s[i:i+2] == 'IT':
#                     i += 2
#             else:
#                 return False
#         else:
#             return False
#     return i == n
# def main():
#     t = int(input())
#     results = []
#     for _ in range(t):
#         n = int(input())
#         s = input().strip()
#         if is_repetitive_string(s):
#             results.append("YES")
#         else:
#             results.append("NO")
#     print("\n".join(results))
# if __name__ == "__main__":
#     main()