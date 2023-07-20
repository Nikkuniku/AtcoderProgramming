from statistics import median
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
B = [(S[i][0]*S[i][2], S[i][1]) for i in range(N)]
B.sort()
if N % 2 == 0:
    X = (B[(N//2)-1][1]+B[N//2][1])/2
else:
    X = B[N//2][1]
ans = 0
for i in range(N):
    a = S[i][0]
    b = S[i][1]
    c = S[i][2]
    ans += max(0, a*(c-abs(X-b)))
print(ans)
