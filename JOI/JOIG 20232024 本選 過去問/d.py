from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
K = 13
pows = [pow(10, i) for i in range(13)]
ans = 0
pre = 0
for a in A:
    for k in range(K):
        idx = bisect_left(B, pows[k] - a)
        ans += k * (idx - pre)
        pre = idx
print(ans)
