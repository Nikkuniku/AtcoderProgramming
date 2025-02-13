N = int(input())
A = list(map(int, input().split()))
ok = [1, 3, 7, 9]
P = [1 << 60] * 10
for i in range(1, 10):
    for k in ok:
        if i >= k:
            P[i] = i - k
ans = sum([P[a] for a in A])
print(ans)
