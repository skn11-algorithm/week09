'''
음주게임
입력 : 수열의 크기n과 게임 라운드 수 k  
       n개의 숫자 xi 
       명령은 C(변경) or P(곱셈) 시작
출력 : 각 테스트마다 곱셈 명령의 결과를 한줄에 모두 출력
아이디어 : 두 가지 쿼리를 실행 - 변경, 곱셈 명령에 따른 출력 뽑아내보자
          세그먼트 트리 문제를 쓰되 구간 곱의 부호만 출력하면 됨


'''

import sys
input = sys.stdin.readline

# 1. 부호 변환
def sign(n) :
  if n > 0 :
    return 1
  elif n < 0 :
    return -1
  return 0

# 트리 생성
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree[node] = tree[node*2] * tree[node*2+1]

# 곱셈 명령
def query(node, start, end, l, r):
    if r < start or end < l:     # 구간이 겹치지 않을때 
        return 1  
    if l <= start and end <= r:  # 구간이 완전 포함될 때 
        return tree[node]
    mid = (start + end) // 2    # 구간이 일부 겹칠 때 왼 - 오 로 재귀 호출
    left = query(node*2, start, mid, l, r)
    right = query(node*2+1, mid+1, end, l, r)
    return left * right

# 변경 명령
def update(node, start, end, idx, value):
    if idx < start or idx > end: # idx가 현재 구간에 없으면 무시
        return
    if start == end:             # 해당 위치 도달하면 값을 변경한다
        tree[node] = value
    else:
        mid = (start + end) // 2
        update(node*2, start, mid, idx, value)
        update(node*2+1, mid+1, end, idx, value)
        tree[node] = tree[node*2] * tree[node*2+1]

while True:
    try:
        n, k = map(int, input().split())
        raw = list(map(int, input().split()))   # 원래 수열
        arr = [sign(x) for x in raw]            # 부호 저장하는 배열
        tree = [1] * (4 * n)                    # 세그먼트 트리를 위한 배열 생성

        build(1, 0, n-1)

        result = []
        for _ in range(k):
            cmd = input().split()
            if cmd[0] == 'C':             
                i = int(cmd[1]) - 1
                v = sign(int(cmd[2]))
                update(1, 0, n-1, i, v)
            else:  # P 명령
                l = int(cmd[1]) - 1
                r = int(cmd[2]) - 1
                res = query(1, 0, n-1, l, r)
                if res > 0:
                    result.append('+')
                elif res < 0:
                    result.append('-')
                else:
                    result.append('0')

        print(''.join(result))
    except:
        break