A, M, L, R = map(int, input().split())
L -= A
R -= A
ans = 0
if R < 0 and L < 0:
    L, R = -R, -L
ans += R // M
if L > 0:
    ans -= (L - 1) // M
else:
    ans += 1
    ans += (-L) // M
print(ans)
