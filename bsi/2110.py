import sys
input = sys.stdin.readline

house, num = map(int, input().split()) 
hs_lst = []
for _ in range(house):
    hs_lst.append(int(input()))
hs_lst.sort()

max_len = hs_lst[-1] - hs_lst[0]
min_len = 1

def can_install(hs_lst, distance, num):  
    count = 1
    current_hs = hs_lst[0]  

    for i in range(1, len(hs_lst)):
        if hs_lst[i] - current_hs >= distance:  
            count += 1
            current_hs = hs_lst[i]
            if count >= num:
                return True
    return False

result = 0
while min_len <= max_len:
    mid = (min_len + max_len) // 2
    if can_install(hs_lst, mid, num): 
        result = mid
        min_len = mid + 1
    else:
        max_len = mid - 1

print(result)