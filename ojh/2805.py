import sys

input=sys.stdin.readline

N,M=map(int,input().rstrip().split()) # 나무의 수, 가져갈 길이
trees=list(map(int,input().rstrip().split()))

def cut(trees,n):
    get=0
    for i in range(N):
        get+=(trees[i]-n if trees[i]-n>=0 else 0)
    return get

start=0
end=max(trees)

result=0
while start<=end:
    mid=(start+end)//2
    get=cut(trees,mid)
    
    if get<M: # 가져가야 하는 길이보다 짧으면, 절단높이 줄여야함
        end=mid-1
    else:
        result=mid # 절단 높이 최댓값 구해야하므로 계속 갱신
        start=mid+1

print(result)




