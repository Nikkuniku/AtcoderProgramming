N = list(input())
for i, v in enumerate(N):
    N[i] = int(v)
ans = "YES" if 3 in N or sum(N) % 3 == 0 else "NO"
print(ans)
