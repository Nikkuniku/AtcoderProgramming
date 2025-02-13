N, M, P = map(int, input().split())
ans = 0
if N - M >= 0:
    ans += 1
else:
    exit(print(0))
ans += (N - M) // P
print(ans)
