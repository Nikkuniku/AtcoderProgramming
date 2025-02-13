N, X, Y, Z = map(int, input().split())
if Y < X:
    X, Y = Y, X
ans = "No"
if X <= Z <= Y:
    ans = "Yes"
print(ans)
