# 두 용액
n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left, right = 0, n - 1
min_diff = float('inf')
ans = (0, 0)

while left < right:
    mix = liquids[left] + liquids[right]

    if abs(mix) < min_diff:
        min_diff = abs(mix)
        ans = (liquids[left], liquids[right])

    if mix < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])