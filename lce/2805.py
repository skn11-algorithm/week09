# 나무자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(tree - mid for tree in trees if tree > mid)

    if total >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)