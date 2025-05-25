import sys
input = sys.stdin.readline  

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
# 부호 값으로 트리를 초기화
def init(start,end,index):
    if start==end:
        tree[index]=sign(nums[start])
        return tree[index]

    mid=(start+end)//2
    left_child=init(start,mid,index*2)
    right_child=init(mid+1,end,index*2+1)
    tree[index]=left_child*right_child

    return tree[index]

def update_tree(start, end, index, target, diff):
    if target < start or target > end:
        return
    
    if start == end:
        tree[index]= sign(diff)
        return 
    
    mid = (start + end) // 2
    update_tree(start, mid, index*2, target, diff)
    update_tree(mid+1, end, index*2+1, target, diff)
    tree[index] = tree[index * 2] * tree[index * 2 + 1]

def find(start,end,index,left,right):
    if left>end or right<start:
        return 1 # 곱 연산에 영향 X
    
    #2. 범위가 완전히 포함되는 경우(left,right 사이에 start,end가 있는 경우)
    if left <=start and end<=right:
        return tree[index]
    
    #3. 범위가 일부만 겹치는 경우
    mid=(start+end)//2
    left_child=find(start,mid,index*2,left,right)
    right_child=find(mid+1,end,index*2+1,left,right)

    return left_child*right_child

try:
    while True:
        line = input()
        if not line:
            break
        N, K = map(int, line.split()) #숫자개수, 명령개수
        nums = [0] + list(map(int,input().rstrip().split()))
        tree = [0] * (4 * N)
        init(0,N,1)

        result=[]
        for _ in range(K):
            order,a,b = input().rstrip().split()
            a,b=int(a),int(b)
            if order=='C': # 숫자 변경, a를 b로
                nums[a]=b
                update_tree(1,N,1,a,b)
            else : # 곱셈, a부터 b까지
                ans=(find(1,N,1,a,b))
                if ans == 0:
                    result.append('0')
                elif ans > 0:
                    result.append('+')
                else:
                    result.append('-')

        print(''.join(result))

except EOFError:
    pass