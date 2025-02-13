X, A, D, N = map(int, input().split())
X -= A
A -= A
if D < 0:
    D *= -1
    X *= -1
if X <= 0:
    ans = -X
elif (N - 1) * D <= X:
    ans = abs((N - 1) * D - X)
else:
    k = X // D
    ans = min(abs(k * D - X), abs((k + 1) * D - X))
print(ans)
