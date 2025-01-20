
class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.tree = [set() for _ in range(4 * n)]  # Use a set to store values in each range
        self._build(0, 0, n - 1)
    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = {self.a[start]}
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self._build(left, start, mid)
            self._build(right, mid + 1, end)
            self.tree[node] = self.tree[left] | self.tree[right]
    def _update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = {value}
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            if idx <= mid:
                self._update(left, start, mid, idx, value)
            else:
                self._update(right, mid + 1, end, idx, value)
            self.tree[node] = self.tree[left] | self.tree[right]
    def _query(self, node, start, end, l, r):
        if start > r or end < l:
            return set()
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        left_result = self._query(left, start, mid, l, r)
        right_result = self._query(right, mid + 1, end, l, r)
        return left_result | right_result
    def update(self, idx, value):
        self._update(0, 0, self.n - 1, idx, value)
    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)
def missing_number_queries(n, q, a, queries):
    seg_tree = SegmentTree(n, a)
    results = []
    for query in queries:
        if query[0] == 1:
            _, x, y = query
            seg_tree.update(x - 1, y)
        elif query[0] == 2:
            _, l, r = query
            present = seg_tree.query(l - 1, r - 1)
            # Find the first missing number in [1, N]
            for i in range(1, n + 1):
                if i not in present:
                    results.append(i)
                    break
    return results
# Input Reading and Processing
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    # Read N and Q
    n, q = map(int, data[:2])
    # Read initial array
    a = list(map(int, data[2:2 + n]))
    # Read queries
    queries = []
    idx = 2 + n
    for _ in range(q):
        queries.append(list(map(int, data[idx:idx + 3])))
        idx += 3
    # Solve
    results = missing_number_queries(n, q, a, queries)
    # Output results
    sys.stdout.write("\n".join(map(str, results)) + "\n")