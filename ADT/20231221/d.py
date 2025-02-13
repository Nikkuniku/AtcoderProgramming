N = int(input())
S = input()
ans = []
for i in range(1, N):
    for k in range(N):
        if k + i > N - 1:
            ans.append(k)
            break
        if S[k] == S[k + i]:
            ans.append(k)
            break
print(*ans, sep="\n")
