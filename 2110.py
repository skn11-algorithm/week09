'''
공유기 설치 
입력 : 집의 개수 n, 공유기의 개수c / 집의 좌표 Xi
출력 : 가장 인접한 공유기 사이의 최대 거리

아이디어 : 집 좌표를 array 정렬 -> 원하는 값을 찾는거니까 공유기 거리를 이진탐색
'''

n, c = map(int, input().split())

array = [int(input()) for _ in range(n)]
array.sort()


# 공유기 거리 최대거리, 최소거리
start = 1
end = array[-1] - array[0]

def search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        now = array[0] # 현재위치를 0번째 인덱스부터 해서 탐색 시작 
        count = 1

        for i in range(1, len(array)):
            if array[i] >= now + mid:
                count += 1
                now = array[i] # 현재 위치 갱신

        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print(search(array, start, end))