# 구간 합 구하기2
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, l, r, diff):
    update_lazy(node, start, end)
    if r < start or end < l:
        return
    if l <= start and end <= r:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start + end) // 2
    update_range(node*2, start, mid, l, r, diff)
    update_range(node*2+1, mid+1, end, l, r, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, l, r):
    update_lazy(node, start, end)
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, l, r) + query(node*2+1, mid+1, end, l, r)

n, m, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
tree = [0] * (4 * (n + 1))
lazy = [0] * (4 * (n + 1))

init(1, 1, n)

for _ in range(m + k):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        _, b, c, d = tmp
        update_range(1, 1, n, b, c, d)
    else:
        _, b, c = tmp
        print(query(1, 1, n, b, c))