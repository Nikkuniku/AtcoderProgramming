S = input()
T = input()
ans = len(S) + 1
for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        break
print(ans)
