# 실버2 2805번 나무 자르기

# 입력
# - 나무 수 n, 상근이가 집으로 가져가려는 나무의 길이 m
# - 나무의 높이 (나무의 높이는 항상 m보다 크거나 같아서 집으로 필요한 나무를 항상 가져갈 수 있음)

# 출력
# - 적어도 m 미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값

# 문제
# - 절단기에 높이 h를 지정해야 하고
# - 높이를 지정하면 땅으로부터 h미터 위로 올라간 다음 연속해 있는 나무 다 절단

# 풀이
# - 이진탐색

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end: 
    mid = (start+end) // 2

    total = 0
    for i in tree:
        if i >= mid:
            total += i - mid
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)