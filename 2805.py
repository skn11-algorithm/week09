'''
나무 자르기

입력 : 각각 다른 길이의 나무의 수 N개, 가져갈 나무의 길이 M / 각 나무의 높이
출력 : m 미터를 가져가기 위한 절단기 높이의 최댓값 구하기
아이디어 : 최소 m을 가져갈 수 있는 철단기 높이를 구해야 하므로 나무의 길이가 m이 되는 경우를 찾는다
'''

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0 # 최종 절단기 높이 

while(start <= end):
    total = 0 # 가져갈 나무의 길이
    mid = (start + end) // 2 # 절단기 높이
    for i in tree:
        if i > mid: # 절단기보다 주어진 나무가 길면 자른 나머지를 total에 추가
            total += i - mid    
    if total < m: # 가져가야 하는 길이 m보다 작은 길이이면
        end = mid - 1 
    else:
        result = mid 
        start = mid + 1 
print(result)