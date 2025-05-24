import sys

input=sys.stdin.readline

N=int(input().rstrip())
solution=list(map(int,input().rstrip().split()))
solution.sort()

start,end=0,N-1
abs_hap=abs(solution[start]+solution[end])
result=[solution[start],solution[end]]

while start<end:
    hap=solution[start]+solution[end]

    if abs(hap)<abs_hap:
        abs_hap=abs(hap)
        result=[solution[start],solution[end]]
        if abs_hap == 0:
            break

    if hap<0:
        start+=1
    else:
        end-=1

print(result[0],result[1])