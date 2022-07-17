from math import gcd
n = int(input())
ans = [10, 15, 6]
nums = set()
for i in range(7, 10001):
    if i % 2 == 0 and i % 3 == 0:
        nums.add(i)
for i in range(11, 10001):
    if i % 2 == 0 and i % 5 == 0:
        nums.add(i)
for i in range(16, 10001):
    if i % 3 == 0 and i % 5 == 0:
        nums.add(i)

nums = list(nums)
for v in nums:
    ans.append(v)
ans = ans[:2500]
print(*ans[:n])

# gcds = set()
# for i in range(n):
#     for j in range(i+1, n):
#         g = gcd(ans[i], ans[j])
#         gcds.add(g)
# print(gcds)
# g = 0
# for v in ans:
#     g = gcd(g, v)
# print(g)
