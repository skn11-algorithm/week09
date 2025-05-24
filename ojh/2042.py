import sys
input=sys.stdin.readline

N,M,K=map(int,input().rstrip().split())
nums=[0]+[ int(input().rstrip()) for _ in range(N)]
tree=[0]*(4*N)


def make_tree(start,end,index):
    if start==end:
        tree[index]=nums[start]
        return tree[index]

    mid=(start+end)//2
    left_child=make_tree(start,mid,index*2)
    right_child=make_tree(mid+1,end,index*2+1)
    tree[index]=left_child+right_child

    return tree[index]

def find(start,end,index,left,right):
    if left>end or right<start:
        return 0 # 합 연산에 영향 X
    
    #2. 범위가 완전히 포함되는 경우(left,right 사이에 start,end가 있는 경우)
    if left <=start and end<=right:
        return tree[index]
    
    #3. 범위가 일부만 겹치는 경우
    mid=(start+end)//2
    left_child=find(start,mid,index*2,left,right)
    right_child=find(mid+1,end,index*2+1,left,right)

    return left_child+right_child


for _ in range(M+K):
    a,b,c=map(int,input().rstrip().split())
    if a==1:
        nums[b]=c
        make_tree(1,N,1)
    elif a==2:
        print(find(1,N,1,b,c))
