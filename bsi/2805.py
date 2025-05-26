# import sys

# input = sys.stdin.readline

# num, leng = map(int, input().split())
# height = list(map(int, input().split()))

# max_height = sum(height) // len(height)
    
# def find(max_height, leng):    
#     k = sum(height) - len(height) * max_height
#     if leng == k:
#         return max_height      
#     elif leng > k:
#         return find((max_height+max(height))//2, leng) // 범위 설정 잘못함
#     elif leng < k:
#         return find((max_height+min(height))//2, leng)

# a = find(max_height, leng)
# print(a)

import sys
input = sys.stdin.readline

def get_wood_length(heights, cut_height):
    """주어진 절단 높이에서 얻을 수 있는 나무 길이를 계산"""
    total = 0
    for height in heights:
        if height > cut_height:
            total += height - cut_height
    return total
# 주어진 cut_height 이상의 나무길이만 고려하여 계산

def solve():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # 이진 탐색 범위 설정: 0~최대 나무 길이까지
    left = 0
    right = max(heights)
    
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        wood_length = get_wood_length(heights, mid)
        
        if wood_length >= m:  # 필요한 나무를 얻을 수 있는 경우
            result = mid  # 현재 높이를 저장
            left = mid + 1  # 더 높은 높이 시도
        else:  # 필요한 나무를 얻을 수 없는 경우
            right = mid - 1  # 더 낮은 높이 시도
    
    print(result)

solve()