import sys

input=sys.stdin.readline

N,M=map(int,input().rstrip().split()) # 나무의 수, 가져갈 길이
trees=list(map(int,input().rstrip().split()))

def cut(trees,n):
    get=0
    for i in range(N):
        get+=(trees[i]-n if trees[i]-n>=0 else 0)
    return get


max_tree=max(trees)
arr=[0]*max_tree

for i in range(1,max_tree):
    arr[i]=cut(trees,i)

    if arr[i]==M:
        print(i)
        break


