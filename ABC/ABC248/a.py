s = list(input())
nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for p in s:
    nums.remove(int(p))
print(min(nums))
