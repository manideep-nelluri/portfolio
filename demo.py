import math
import sys
input = sys.stdin.read

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = math.gcd(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, 2*node+1, start, mid)
            else:
                self.update(idx, val, 2*node+2, mid+1, end)

            self.tree[node] = math.gcd(self.tree[2*node+1], self.tree[2*node+2])

    def query(self, l, r, node, start, end):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_gcd = self.query(l, r, 2*node+1, start, mid)
        right_gcd = self.query(l, r, 2*node+2, mid+1, end)

        return math.gcd(left_gcd, right_gcd)


# -------- Input Handling --------
data = input().split()
n, q = map(int, data[:2])
arr = list(map(int, data[2:2+n]))

seg_tree = SegmentTree(arr)

index = 2 + n
results = []

for _ in range(q):
    t = int(data[index])
    
    if t == 1:
        i = int(data[index+1]) - 1
        x = int(data[index+2])
        seg_tree.update(i, x, 0, 0, n-1)
        index += 3
        
    else:
        l = int(data[index+1]) - 1
        r = int(data[index+2]) - 1
        results.append(str(seg_tree.query(l, r, 0, 0, n-1)))
        index += 3

print("\n".join(results))