N, X, Y, Z = map(int, input().split())
if X > Y:
    X, Y = Y, X
ans = "Yes" if X <= Z <= Y else "No"
print(ans)
