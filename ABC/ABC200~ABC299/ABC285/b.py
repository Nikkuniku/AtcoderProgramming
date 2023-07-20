N = int(input())
S = input()
ans = []
for i in range(1, N):
    for k in range(N):
        if k+i > N-1:
            break
        if S[k] == S[k+i]:
            break
    ans.append(k)
print(*ans, sep="\n")
