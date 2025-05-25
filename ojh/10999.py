import sys
input = sys.stdin.readline

def main():
    # 세그먼트 트리 초기화 ------------------------
    def init(start, end, index):
        # start, end: 지금 이 노드가 관리하는 배열 구간
        # index: 세그먼트 트리에서 현재 노드의 인덱스

        # 구간이 1개 원소라면 해당 값을 저장
        if start == end:
            tree[index] = nums[start]
            return
        
        # 구간이 여러개의 원소라면
        # 중간을 나눠서 좌측/우측 트리 만들고
        mid = (start + end) // 2
        init(start, mid, index*2)
        init(mid+1, end, index*2+1)

        # 합을 부모 노드에 저장
        tree[index] = tree[index*2] + tree[index*2+1]

    # Lazy 값 전파 ------------------------
    def propagate(index, start, end):
        # 현재 노드(index)가 담당하는 구간 [start, end]
        # 현재 노드에 Lazy 값이 있다면 트리에 반영
        if lazy[index] != 0:
            # 원소 개수 * 변화량 = 전체변화량
            tree[index] += (end - start + 1) * lazy[index]
            # 자식 노드가 있으면 Lazy 값을 자식에게 넘김
            if start != end:
                lazy[index*2] += lazy[index]
                lazy[index*2+1] += lazy[index]
            # 현재 노드의 지연 값은 반영 완료했으므로 초기화
            lazy[index] = 0

    # 범위 업데이트 ------------------------
    def update_range(start, end, index, left, right, diff):
        # start, end: 현재 노드가 담당하는 구간
        # index: 현재 노드의 인덱스
        # left, right: 업데이트 하려는 실제 구간
        # diff: 변경할 값 (더할 값)

        # 해당 노드에 미뤄둔 값이 있다면 반영
        propagate(index, start, end)

        # 구간이 겹치지 않으면 무시
        if right < start or end < left:
            return
        
        # 구간이 완전히 포함되면
        if left <= start and end <= right:
            # 바로 변화량을 반영
            tree[index] += (end - start + 1) * diff
            if start != end:
                # 추후에 반영할 수 있도록 lazy 배열에 diff 누적
                lazy[index*2] += diff
                lazy[index*2+1] += diff
            return
        
        # 일부만 겹치면 자식 노드로 내려가서 분할 업데이트
        mid = (start + end) // 2
        update_range(start, mid, index*2, left, right, diff)
        update_range(mid+1, end, index*2+1, left, right, diff)
        
        # 업데이트가 끝나면, 자식들의 값을 다시 합쳐서 내 값을 갱신
        tree[index] = tree[index*2] + tree[index*2+1]

    # 구간 합 쿼리 ------------------------
    def query(start, end, index, left, right):
        # start, end: 현재 노드가 담당하는 구간
        # index: 현재 노드의 인덱스
        # left, right: 구간 합을 구하려는 범위

        # propagate를 먼저 호출 → lazy 값이 있다면 반영
        propagate(index, start, end)

        # 구간이 겹치지 않으면 0 반환
        if right < start or end < left:
            return 0 # 합을 해도 반영 X
        
        # 구간이 완전히 포함되면: 현재 노드의 값을 반환
        if left <= start and end <= right:
            return tree[index]
        
        # 일부만 겹치면
        mid = (start + end) // 2
        # 자식 노드들로 내려가서 좌측+우측 결과를 합산
        return query(start, mid, index*2, left, right) + query(mid+1, end, index*2+1, left, right)

    #  답 계산하기 ------------------------
    N, M, K = map(int, input().split()) #숫자개수, 변경횟수, 구간합 횟수
    nums = [0] + [int(input()) for _ in range(N)]
    tree = [0] * (4 * N)
    lazy = [0] * (4 * N)

    init(1, N, 1)

    for _ in range(M + K): # 숫자 변경횟수 + 구간합 구할 횟수
        cmd = list(map(int, input().split()))
        if cmd[0] == 1: # 1이면 숫자변경
            b, c, d = cmd[1], cmd[2], cmd[3]
            update_range(1, N, 1, b, c, d)
        else: # 2이면 구간합 구하기
            b, c = cmd[1], cmd[2]
            print(query(1, N, 1, b, c))

if __name__ == "__main__":
    main()
