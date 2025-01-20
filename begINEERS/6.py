# Question 6
# 30/100
from collections import deque
def get_all_transformations(s):
    """
    Generates all possible transformations of a string by swapping adjacent pairs of 'A' and 'B' within a substring of length 3.
    Args:
        s: The input string.
    Returns:
        A list of all possible transformed strings.
    """
    transformations = []
    n = len(s)
    for i in range(n - 2):
        substring = s[i:i+3]
        if substring in {"AAB", "BAA", "BBA", "ABB"}:
            transformations.append(s[:i] + substring[::-1] + s[i+3:])
    return transformations
def min_operations(s1, s2):
    """
    Calculates the minimum number of operations required to transform string s1 into string s2.
    Args:
        s1: The initial string.
        s2: The target string.
    Returns:
        The minimum number of operations, or -1 if it's not possible to transform s1 into s2.
    """
    if s1 == s2:
        return 0
    queue = deque([(s1, 0)])
    visited = set([s1])
    while queue:
        current, ops = queue.popleft()
        for next_string in get_all_transformations(current):
            if next_string == s2:
                return ops + 1
            if next_string not in visited:
                visited.add(next_string)
                queue.append((next_string, ops + 1))
    return -1
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s1, s2 = input().split()
        result = min_operations(s1, s2)
        print(result)