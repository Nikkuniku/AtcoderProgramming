N = int(input())
S = [(input(), i) for i in range(N)]
S.sort()
ans = [0]*N
for i in range(N):
    s, j = S[i]
    if i < N-1:
        t, m = S[i+1]
        cnt = 0
        for k in range(len(s)):
            if s[k] == t[k]:
                cnt += 1
            else:
                break
        ans[j] = max(ans[j], cnt)
        ans[m] = max(ans[m], cnt)

print(*ans, sep="\n")
