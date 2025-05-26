# 두 용액
'''
입력 : 전체 용액의 수 n (2~100,000) / 용액의 특성값 정수들
출력 : 특성값이 0에 가까운 용액을 만들어내는 두 용액의 특성값(오름차순 sort)

아이디어 : 마찬가지로 이진탐색을 통해 합이 0에 가까운 양쪽 두 값을 "투포인터" 탐색
            -> 인덱스를 기준으로 양쪽 탐색하며 0에 수렴하자!!
'''

n = int(input())
array = sorted(list(map(int, input().split())))

# 각 인덱스 값 설정
start = 0
end = n-1
smallest = float('inf') 

while start < end:
    now = array[start] + array[end] # 용액 혼합
    if abs(now) < smallest:
        smallest = abs(now)
        new_smallest = [array[start], array[end]]
    if now < 0:  # 0보다 작으면 더 큰값 필요하므로 포인터 이동 s +
        start += 1
    elif now > 0:  # 0보다 크면  " e -
        end -= 1
    else:
        break

new_smallest.sort() # 갱신된 두 용액 오름차순
print(new_smallest[0], new_smallest[1])

