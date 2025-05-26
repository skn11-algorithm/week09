import sys
input=sys.stdin.readline

N,C=map(int,input().rstrip().split())
home=[ int(input().rstrip()) for _ in range(N)]
home.sort()

# 공유기의 최소거리 1, 최대가능거리 (첫집과 끝집 차이)
start=1
end=home[-1]-home[0]
result=0

# 현재 거리에서공유기 C개 설치 가능한지 확인
# 가능하면 d를 늘리고, 불가능하면 d를 줄임
while start<=end:
    mid=(start+end)//2 # 시도할 거리
    current=home[0] # 첫 집에 공유기 설치
    count=1 # 설치한 공유기 수

    for i in range(1,len(home)):
        if home[i]>= current+mid :
            count+=1
            current=home[i]

    if count>=C:
        result=mid
        start=mid+1
    else: # 설치 불가 -> 거리 줄이기
        end=mid-1

print(result)