N, X = map(int, input().split())
A = list(map(int, input().split()))
X -= 1
known = [False]*N
now = X
ans = 1
while 1:
    P = A[now]-1
    known[now] = True
    if known[P]:
        break
    else:
        now = P
        ans += 1
print(ans)
