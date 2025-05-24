import sys
input = sys.stdin.readline

num = int(input())
lst = list(map(int,input().split()))
lst.sort()
dic = {}

for i in lst:
    for j in lst:
        if i == j:
            continue
        k = i + j
        dic[k] = [i, j]

sorted_dict = dict(sorted(dic.items(), key=lambda x: abs(x[0])))
print(*list(sorted_dict.values())[0]) 

#  메모리 초과 문제 해결안
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    left = 0
    right = n - 1
    
    min_sum = float('inf')
    result = [arr[left], arr[right]]
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        # 현재 합이 더 0에 가까우면 결과 업데이트
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = [arr[left], arr[right]]
        
        # 포인터 이동
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:  # current_sum == 0인 경우 (최적해)
            break
    
    print(result[0], result[1])

solve()

# 원본 코드의 수정된 버전 (딕셔너리 방식 유지)
def solve_with_dict():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    min_sum = float('inf')
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):  # i+1부터 시작하여 중복 방지
            current_sum = arr[i] + arr[j]
            
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                result = [arr[i], arr[j]]
    
    print(result[0], result[1])

# solve_with_dict()  # 이 방법도 사용 가능