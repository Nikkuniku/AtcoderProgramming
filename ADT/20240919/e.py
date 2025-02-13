N, K = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 0
for i in range(1 << N):
    tmp = [0] * 26
    for j in range(N):
        if i & (1 << j):
            for s in S[j]:
                tmp[ord(s) - 97] += 1
    ans = max(ans, tmp.count(K))
print(ans)
