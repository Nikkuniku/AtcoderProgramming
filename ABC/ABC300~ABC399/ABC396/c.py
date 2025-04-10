from itertools import accumulate

N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))
B.sort(reverse=True)
W.sort(reverse=True)
cum_W = list(accumulate(W, initial=0))
for i in range(1, len(cum_W)):
    cum_W[i] = max(cum_W[i], cum_W[i - 1])
ans = 0
temp = 0
for i, v in enumerate(B):
    temp += v
    ans = max(ans, temp + cum_W[min(i + 1, M)])
print(ans)
