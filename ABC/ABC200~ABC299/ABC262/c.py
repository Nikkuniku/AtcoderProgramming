from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i] == i+1:
        b.append(a[i])
b.sort()
ans = 0
for i in range(n):
    if a[i] == i+1:
        idx = bisect_right(b, a[i])
        ans += len(b)-idx
    else:
        k = a[i]
        if min(a[i], a[k-1]) == i+1 and max(a[i], a[k-1]) == k:
            ans += 1

print(ans)
