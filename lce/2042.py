# 구간 합 구하기
import sys
input = sys.stdin.read
data = input().split()

n, m, k = map(int, data[:3])
arr = list(map(int, data[3:3 + n]))
queries = data[3 + n:]

size = 1
while size < n:
    size *= 2
tree = [0] * (2 * size)

def build():
    for i in range(n):
        tree[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(index, value):
    idx = size + index
    diff = value - tree[idx]
    while idx >= 1:
        tree[idx] += diff
        idx //= 2

def query(l, r):
    l += size
    r += size
    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

build()
output = []
i = 0
while i < len(queries):
    a, b, c = int(queries[i]), int(queries[i+1]), int(queries[i+2])
    if a == 1:
        update(b - 1, c)
    else:
        output.append(str(query(b - 1, c - 1)))
    i += 3

print('\n'.join(output))