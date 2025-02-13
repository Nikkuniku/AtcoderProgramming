A, M, L, R = map(int, input().split())
k = (L - A) // M
r = (R - A) // M
ans = r - k
if A + k * M == L:
    ans += 1
print(ans)
