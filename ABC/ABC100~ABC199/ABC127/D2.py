from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
for _ in range(M):
    b, c = map(int, input().split())
    C[c] += b
ans = 0
cnt = 0
values = sorted([(k, v) for k, v in C.items()], reverse=True)
for k, v in values:
    tmp = N - cnt
    if tmp > 0:
        if v >= tmp:
            ans += tmp * k
            cnt += tmp
        else:
            ans += v * k
            cnt += v
print(ans)
