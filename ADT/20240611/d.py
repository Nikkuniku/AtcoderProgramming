N = int(input())
S = list(input())
ans = []
for i in range(N):
    cnt = 0
    for k in range(N):
        if i + k > N - 1:
            break
        if S[i + k] != S[k]:
            cnt += 1
        else:
            break
    ans.append(cnt)
print(*ans[1:], sep="\n")
