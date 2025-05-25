import sys
input = sys.stdin.readline

len_num, num_round = map(int, input().split())
num_lst = [0] + [int(input().rstrip()) for _ in range(len_num)]  
tree = [0] * (len_num * 4)

# 트리 생성 함수
def init(start, end, index):  # 숫자 배열의 start,end, 트리의 인덱스
    if start == end:
        tree[index] = num_lst[start]
        return tree[index]
    
    mid = (start + end) // 2
    left_child = init(start, mid, index * 2)
    right_child = init(mid + 1, end, index * 2 + 1)
    tree[index] = left_child * right_child  # 구간 합이므로 합을 저장
    return tree[index]

# 값 업데이트 함수
def update(start, end, index, target, value):
    if start == end:
        tree[index] = value
        return
    
    mid = (start + end) // 2
    if target <= mid:
        update(start, mid, index * 2, target, value)
    else:
        update(mid + 1, end, index * 2 + 1, target, value)
    
    tree[index] = tree[index * 2] + tree[index * 2 + 1]

# 구간 합 찾기
def find_sum(start, end, index, left, right):
    # 1. 범위가 전혀 겹치지 않는 경우
    if left > end or right < start:
        return 0
    
    # 2. 범위가 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[index]
    
    # 3. 범위가 일부만 겹치는 경우
    mid = (start + end) // 2
    left_child = find_sum(start, mid, index * 2, left, right)
    right_child = find_sum(mid + 1, end, index * 2 + 1, left, right)
    return left_child + right_child

# 트리 생성
init(1, len_num, 1)

# 쿼리 처리
for _ in range(num_round):  # * → _, num*changes → num_changes
    a, b, c = input().rstrip().split()
    if a == 'C':  # 값 변경
        num_lst[b] = c  # num_lst[c] → c (값을 c로 변경)
        update(1, len_num, 1, b, c)
    else:  # 구간 합 구하기
        print(find_sum(1, len_num, 1, b, c))



# 무한 오버플로우 방지: 모든 수를 부호로만 저장
# 정확한 구간 곱 계산: 세그먼트 트리로 O(log N) 시간에 처리
# 올바른 테스트 케이스 처리: EOF까지 입력 받기
# 정확한 출력 형식: 모든 P 명령의 결과를 한 줄에 출력