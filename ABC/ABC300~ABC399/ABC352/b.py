S = input()
T = input()
now = 0
ans = []
for i in range(len(T)):
    if T[i] == S[now]:
        ans.append(i + 1)
        now += 1
    if now == len(S):
        break
print(*ans)
