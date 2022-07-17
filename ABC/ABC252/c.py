n = int(input())
s = []
for _ in range(n):
    s.append(list(input()))
nums = [[0]*10 for _ in range(10)]
for i in range(n):
    for j in range(10):
        p = int(s[i][j])
        nums[p][j] += 1
ans = 10**18
for i in range(10):
    tmp = 0
    m = max(nums[i])
    idx = -1
    for j in range(10):
        if nums[i][j] == m:
            idx = j
    ans = min(idx + (nums[i][idx]-1)*10, ans)
print(ans)
