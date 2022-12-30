from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
b = a.copy()
a = sorted(list(set(a)))
m = len(a)

ans = [0]*n
for p in b:
    idx = bisect_right(a, p)
    ans[m-idx] += 1

print(*ans, sep="\n")
