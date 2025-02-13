S = input()
T = input()
ans = []
i = 0
for j in range(len(T)):
    if S[i] == T[j]:
        ans.append(j + 1)
        i += 1
    if i == len(S):
        break
print(*ans)
