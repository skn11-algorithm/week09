# 2470번 두 용액

# 입력
# - 전체 용액의 수 n
# - 용액의 특성값을 나타내는 n개의 정수

# 출력
# - 특성값이 0에 가장 가까운 두 용액의 특성값 출력
# - 출력해야 하는 두 용액은 특성값의 오름차순
# - 0에 가까운 용액을 만들어내는 경우가 두 개 이상이면 아무거나 하나 출력

import sys

input = sys.stdin.readline

n = input()
solutions = list(map(int, input().split()))

solutions = sorted(solutions)

start = 0
end = len(solutions)-1

zero = 1e7
answer = []
while start < end:
    sum = solutions[start] + solutions[end]

    if abs(sum) < zero:
        zero = abs(sum)
        answer.clear()
        answer.append(solutions[start])
        answer.append(solutions[end])
    
    if sum < 0:
        start = start + 1
    else:
        end = end - 1

answer = sorted(answer)
print(answer[0], answer[1])


