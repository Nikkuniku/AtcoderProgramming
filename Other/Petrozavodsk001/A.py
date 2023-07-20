from math import gcd
X, Y = map(int, input().split())
ans = X*Y//(gcd(X, Y)) - X
if ans % X == 0 and ans % Y == 0:
    ans = -1
print(ans)
