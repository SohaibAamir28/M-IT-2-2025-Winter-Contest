def is_repetitive(s):
    # Check if the string starts with M
    if not s.startswith("M"):
        return False
    i = 1
    n = len(s)
    # Check the remaining part of the string
    while i < n:
        if i + 1 < n and s[i:i+2] == "IT":
            i += 2
        else:
            return False
    return True
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])  # Number of test cases
    results = []
    index = 1
    for _ in range(t):
        length = int(data[index])  # Length of the string (not used)
        s = data[index + 1]  # The string itself
        index += 2
        # Check if the string is repetitive
        if is_repetitive(s):
            results.append("YES")
        else:
            results.append("NO")
    # Print all results at once
    sys.stdout.write("\n".join(results) + "\n")