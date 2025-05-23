# 2110번 공유기 설치

# 입력
# - 집의 개수 n, 공유기의 개수 c
# - n개의 줄에는 집의 좌표를 나타내는 xi가 하나씩 

# 출력
# - 첫째줄에 가장 인접한 두 공유기 사이의 최대 거리

# 문제
# - 집 n개가 수직선 위에 있고 각 좌표는 xi
# - 공유기 c개를 설치하려는데 최대한 많은 곳에서 와이파이를 사용해야 해서 한 집에는 공유를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 걸이를 가능한 크게 해 설치하려 함
# - c개의 공유기를 n개의 집에 적당히 설치해서 가장 인접한 공유기 사이 거리를 최대로 하는 코드

# 흐름
# - 일직선에 집이 있는거니까 일단 sort
# - 가장 인접한 두 공유기 사이 거리가 최대로 하는게 뭘까
# - 인접한 두 공유기 사이 거리를 출력하는거네

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = []
for i in range(n):
    x = int(input())
    houses.append(x)

houses.sort()

start = 1   # 최소 거리
end = houses[-1] - houses[0]        # 최대 거리
answer = 0
while start < end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if (houses[i] >= current + mid):
            count += 1
            current = houses[i]
    
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(end)

