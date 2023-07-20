N = int(input())
A, B = map(int, input().split())
C = int(input())
res = []
D = [int(input()) for _ in range(N)]
D.sort(reverse=True)
price = A
for k in range(N+1):
    price = A+k*B
    callory = C+sum(D[:k])
    res.append(callory//price)
ans = max(res)
print(ans)
