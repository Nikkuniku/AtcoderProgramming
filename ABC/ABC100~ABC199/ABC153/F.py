from bisect import bisect_right


def ceil(a, b):
    return -(-a//b)


N, D, A = map(int, input().split())
monster = [list(map(int, input().split())) for _ in range(N)]
monster.sort(key=lambda x: x[0])
X = [m[0] for m in monster]
H = [m[1] for m in monster]
ans = [0]*(N+1)
answer = 0
for i in range(N):
    x, h = X[i], H[i]
    cnt = ans[i]
    if cnt*A < h:
        k = ceil((h-cnt*A), A)
        idx = bisect_right(X, x+2*D)
        ans[i] += k
        ans[idx] -= k
        answer += k
    ans[i+1] += ans[i]
print(answer)
