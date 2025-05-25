import sys
import math

input = sys.stdin.readline

N, M, K = map(int,input().split())
node = 2**(math.ceil(math.log2(N)))
tree = [0 for i in range(node*2)]
lazy = [0 for i in range(node*2)]

for i in range(N):
  tree[node+i] = int(input())


def init(index):
  if index<node:
    tree[index] = init(index*2) + init(index*2+1)
  return tree[index]


def updateLazy(start, end, index):
  if lazy[index]:
    tree[index] += (end-start+1) * lazy[index]
    if start!=end:
      lazy[index*2] += lazy[index]
      lazy[index*2+1] += lazy[index]
    lazy[index] = 0
        

def updateRange(targetStart, targetEnd, start, end, index, val):
  updateLazy(start, end, index)
  if start > targetEnd or end < targetStart:
    return 
    
  if targetStart <= start and end <= targetEnd:
    tree[index] += (end-start+1) * val
    if start != end:
      lazy[index*2] += val
      lazy[index*2+1] += val
    return 
    
  mid = (start + end) // 2
  updateRange(targetStart, targetEnd, start, mid, index*2, val) 
  updateRange(targetStart, targetEnd, mid + 1, end, index*2+1, val)
  tree[index] = tree[index*2] + tree[index*2+1]
  

def printSum(targetStart, targetEnd, start, end, index):
  updateLazy(start, end, index)
  if start > targetEnd or end < targetStart:
    return 0

  if targetStart <= start and end <= targetEnd:
    return tree[index]

  mid = (start + end) // 2
  return printSum(targetStart, targetEnd, start, mid, index*2) + printSum(targetStart, targetEnd, mid + 1, end, index*2+1)

init(1)


for i in range(M+K):
  abc = list(map(int,input().split()))
  if abc[0] == 1:
    updateRange(abc[1], abc[2], 1, node, 1, abc[3])
  else:
    print(printSum(abc[1], abc[2], 1, node, 1))