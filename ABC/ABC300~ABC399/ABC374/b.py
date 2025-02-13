S = input()
T = input()
ans = 0 if S == T else -1
S += "*" * 100
T += "*" * 100
for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        break
print(ans)
