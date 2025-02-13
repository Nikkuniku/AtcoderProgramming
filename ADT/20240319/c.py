N, X = map(int, input().split())
X -= 1
A = list(map(int, input().split()))
known = [0] * N
ans = 0
while known[X] == 0:
    ans += 1
    known[X] = 1
    X = A[X] - 1
print(ans)
