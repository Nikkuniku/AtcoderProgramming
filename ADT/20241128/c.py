A, M, L, R = map(int, input().split())
L -= A
R -= A
if L <= 0 and R <= 0:
    L, R = -R, -L
ans = R // M
if L > 0:
    ans -= (L - 1) // M
elif L < 0:
    ans += 1
    ans += abs(L) // M
elif L == 0:
    ans += 1
print(ans)
