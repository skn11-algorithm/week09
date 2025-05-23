# 공유기 설치
n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))

low, high = 1, houses[-1] - houses[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    count = 1
    last = houses[0]

    for i in range(1, n):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    if count >= c:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)