'''
구간 합 구하기 
입력 : 수 개수 n, 수 변경횟수 m, 구간의 합 구하는 횟수 k / a, b, c
출력 : a:1 == b번째 값을 c로 교환 a:2== b번째~C번째 합
아이디어 : 배열이 계속 바뀐다..??? 세그먼트 트리를 사용해야 한다. 
'''

import sys
input=sys.stdin.readline


# start, end: 숫자 배열의 인덱스
# idx: 세그먼트 트리의 인덱스 (1부터)
def make_tree(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = make_tree(start, mid, idx * 2) + make_tree(mid + 1, end, idx * 2 + 1)
    return tree[idx]


# target: 수정할 값의 숫자 배열 인덱스
# value: 수정할 값 (기존 값에 얼만큼 더해야 하는지의 값)
def update_tree(start, end, idx, target, value):
    if target < start or target > end:
        return
    
    tree[idx] += value
    if start == end:
        return
    
    mid = (start + end) // 2
    update_tree(start, mid, idx * 2, target, value)
    update_tree(mid + 1, end, idx * 2 + 1, target, value)


# left, right: 구하고자 하는 범위
def sum_tree(start, end, idx, left, right):
    if right < start or left > end:
        return 0

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return sum_tree(start, mid, idx * 2, left, right) + sum_tree(mid + 1, end, idx * 2 + 1, left, right)


N, M, K = map(int, input().split())
arr = []
tree = [0] * (N * 4)  # 충분한 트리 공간 확보
for _ in range(N):
    arr.append(int(input()))

make_tree(0, N-1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(0, N-1, 1, b-1, c - arr[b-1])
        arr[b-1] = c  # 기존 숫자 배열 값 변경
    else:
        print(sum_tree(0, N-1, 1, b-1, c-1))