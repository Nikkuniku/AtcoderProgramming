N = int(input())
A = list(map(int, input().split()))
X = int(input())
Y = 0
ans, q = divmod(X, sum(A))
Y = sum(A)*ans
ans *= N
if Y <= X:
    for i in range(N):
        Y += A[i]
        ans += 1
        if Y > X:
            break
print(ans)
