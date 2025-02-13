S = input()
T = input()
ans = -1
for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        break
else:
    ans = len(S) + 1
print(ans)
