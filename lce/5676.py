# 음주코딩
import sys
input = sys.stdin.readline

def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    return 0

def build():
    for i in range(n):
        tree[size + i] = sign(nums[i])
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] * tree[2 * i + 1]

def update(i, val):
    i += size
    tree[i] = sign(val)
    while i > 1:
        i //= 2
        tree[i] = tree[2 * i] * tree[2 * i + 1]

def query(l, r):
    l += size
    r += size
    res = 1
    while l <= r:
        if l % 2 == 1:
            res *= tree[l]
            l += 1
        if r % 2 == 0:
            res *= tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

while True:
    try:
        line = input()
        if not line:
            break
        n, k = map(int, line.split())
        nums = list(map(int, input().split()))
        size = 1
        while size < n:
            size *= 2
        tree = [1] * (2 * size)

        build()
        result = []
        for _ in range(k):
            cmd = input().split()
            if cmd[0] == 'C':
                idx, val = int(cmd[1]) - 1, int(cmd[2])
                update(idx, val)
            else:
                l, r = int(cmd[1]) - 1, int(cmd[2]) - 1
                res = query(l, r)
                if res > 0:
                    result.append('+')
                elif res < 0:
                    result.append('-')
                else:
                    result.append('0')
        print(''.join(result))
    except:
        break