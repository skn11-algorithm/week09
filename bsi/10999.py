# import sys
# input = sys.stdin.readline

# len_num, num_changes, num_add = map(int, input().split())
# num_lst = [0] + [int(input().rstrip()) for _ in range(len_num)]  
# tree = [0] * (len_num * 4)

# # 트리 생성 함수
# def init(start, end, index):  # 숫자 배열의 start,end, 트리의 인덱스
#     if start == end:
#         tree[index] = num_lst[start]
#         return tree[index]
    
#     mid = (start + end) // 2
#     left_child = init(start, mid, index * 2)
#     right_child = init(mid + 1, end, index * 2 + 1)
#     tree[index] = left_child + right_child  # 구간 합이므로 합을 저장
#     return tree[index]

# # 값 업데이트 함수
# def update(start, end, index, target, value):
#     if start == end:
#         tree[index] = value
#         return
    
#     mid = (start + end) // 2
#     if target <= mid:
#         update(start, mid, index * 2, target, value)
#     else:
#         update(mid + 1, end, index * 2 + 1, target, value)
    
#     tree[index] = tree[index * 2] + tree[index * 2 + 1]

# # 구간 합 찾기
# def find_sum(start, end, index, left, right):
#     # 1. 범위가 전혀 겹치지 않는 경우
#     if left > end or right < start:
#         return 0
    
#     # 2. 범위가 완전히 포함되는 경우
#     if left <= start and end <= right:
#         return tree[index]
    
#     # 3. 범위가 일부만 겹치는 경우
#     mid = (start + end) // 2
#     left_child = find_sum(start, mid, index * 2, left, right)
#     right_child = find_sum(mid + 1, end, index * 2 + 1, left, right)
#     return left_child + right_child

# # 트리 생성
# init(1, len_num, 1)

# # 쿼리 처리 : 시간초과 이유
# for _ in range(num_changes + num_add):  # * → _, num*changes → num_changes
#     lstlst = list(map(int, input().rstrip().split()))
#     if lstlst[0] == 1:  # 값 변경
#         for k in range(lstlst[1], lstlst[2]+1):
#             num_lst[k] = num_lst[k] + lstlst[3]  # num_lst[c] → c (값을 c로 변경)
#             update(1, len_num, 1, lstlst[1], lstlst[2])
#     else:  # 구간 합 구하기
#         print(find_sum(1, len_num, 1, lstlst[1], lstlst[2]))

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (4 * n)
lazy = [0] * (4 * n)

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += lazy[node] * (end - start + 1)
        if start != end:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, l, r, val):
    propagate(node, start, end)
    if start > r or end < l:
        return
    if start >= l and end <= r:
        lazy[node] += val
        propagate(node, start, end)
        return
    
    mid = (start + end) // 2
    update_range(2 * node, start, mid, l, r, val)
    update_range(2 * node + 1, mid + 1, end, l, r, val)
    
    propagate(2 * node, start, mid)
    propagate(2 * node + 1, mid + 1, end)
    tree[node] = tree[2 * node] + tree[2 * node + 1]

def query_range(node, start, end, l, r):
    if start > r or end < l:
        return 0
    propagate(node, start, end)
    if start >= l and end <= r:
        return tree[node]
    
    mid = (start + end) // 2
    left_sum = query_range(2 * node, start, mid, l, r)
    right_sum = query_range(2 * node + 1, mid + 1, end, l, r)
    return left_sum + right_sum

# 트리 초기화
build(1, 0, n - 1)

# 쿼리 처리
for _ in range(m + k):
    query = list(map(int, input().split()))
    
    if query[0] == 1:  # 구간 업데이트
        _, b, c, d = query
        update_range(1, 0, n - 1, b - 1, c - 1, d)
    else:  # 구간 합 쿼리
        _, b, c = query
        print(query_range(1, 0, n - 1, b - 1, c - 1))