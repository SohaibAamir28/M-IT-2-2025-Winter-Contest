from collections import deque
def get_all_transformations(s):
    transformations = []
    n = len(s)
    for i in range(n - 2):
        substring = s[i:i+3]
        if substring == "AAB":
            new_s = s[:i] + "BAA" + s[i+3:]
            transformations.append(new_s)
        elif substring == "BAA":
            new_s = s[:i] + "AAB" + s[i+3:]
            transformations.append(new_s)
        elif substring == "BBA":
            new_s = s[:i] + "ABB" + s[i+3:]
            transformations.append(new_s)
        elif substring == "ABB":
            new_s = s[:i] + "BBA" + s[i+3:]
            transformations.append(new_s)
    return transformations
def min_operations(s1, s2):
    if s1 == s2:
        return 0
    queue = deque([(s1, 0)])
    visited = {s1}
    while queue:
        current, ops = queue.popleft()
        for next_string in get_all_transformations(current):
            if next_string == s2:
                return ops + 1
            if next_string not in visited:
                visited.add(next_string)
                queue.append((next_string, ops + 1))
    return -1
def main():
    T = int(input())
    for _ in range(T):
        s1, s2 = input().split()
        result = min_operations(s1, s2)
        print(result)
if __name__ == "__main__":
    main()