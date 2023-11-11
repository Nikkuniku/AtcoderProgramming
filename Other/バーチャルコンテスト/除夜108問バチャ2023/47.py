X, Y, Z = map(int, input().split())
if X < 0:
    X *= -1
    Y *= -1
    Z *= -1

ans = -1
if abs(X) < abs(Y) or X*Y < 0:
    ans = abs(X)
elif Z < Y < X:
    if X*Z < 0:
        ans = abs(X)+2*abs(Z)
    else:
        ans = abs(X)
print(ans)
