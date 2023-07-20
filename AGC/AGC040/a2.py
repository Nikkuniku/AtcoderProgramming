S = input()
N = len(S)
ans = [0]*(N+1)
for i in range(N):
    if S[i] == '<':
        ans[i+1] = ans[i]+1
for i in range(N-1, -1, -1):
    if S[i] == '>':
        if ans[i] > ans[i+1]:
            continue
        ans[i] = ans[i+1]+1
print(sum(ans))
